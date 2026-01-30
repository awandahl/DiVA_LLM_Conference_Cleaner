#!/usr/bin/env python3
import pandas as pd
from .config import MAX_ROWS, SHOW_EVERY
from .db_io import connect, fetch_conferences, write_parsed_table
from .regex_utils import (
    looks_like_conference_string,
    looks_like_has_date,
    derive_dates_from_conf_dates,
    extract_conf_order,
    normalize_conf_name,
)
from .llm_parse import parse_with_llm
from .llm_series import find_series_candidates, choose_series_with_llm


def main():
    con = connect()
    df = fetch_conferences(con, MAX_ROWS)
    total = len(df)
    print(f"Fetched {total} conference rows for parsing")

    rows = []
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        raw = row["conference"]
        pid = int(row["pid"])
        name_seq = int(row["name_seq"])

        show_stream = (i % SHOW_EVERY == 0)

        print(f"\n=== {i}/{total} PID {pid} name_seq {name_seq} ===")
        print("RAW:", raw)

        if looks_like_conference_string(raw) and looks_like_has_date(raw):
            if show_stream:
                print("LLM output (streaming):")
            parsed = parse_with_llm(raw, show_stream=show_stream)
        else:
            parsed = {
                "conf_name": normalize_conf_name(raw),
                "conf_place": "",
                "conf_dates": "",
                "note": "no date detected or skipped by heuristic",
            }

        b_day, b_month, b_year, e_day, e_month, e_year = derive_dates_from_conf_dates(
            parsed["conf_dates"]
        )
        conf_order = extract_conf_order(parsed["conf_name"])

        # dblp series matching temporarily disabled
        series_slug = None
        stream_iri = None
        series_name = None
        series_reason = "dblp lookup disabled"

        print(
            "PARSED:",
            f"name='{parsed['conf_name']}' | place='{parsed['conf_place']}' | "
            f"dates='{parsed['conf_dates']}' | order={conf_order}",
        )
        if parsed.get("note"):
            print("NOTE:", parsed["note"])

        print("DBLP: lookup disabled")

        """
        # dblp candidates + LLM choice        
        candidates = find_series_candidates(con, parsed["conf_name"])
        series_slug, stream_iri, series_name, series_reason = choose_series_with_llm(
            parsed["conf_name"], parsed["conf_dates"], candidates
        )

        print(
            "PARSED:",
            f"name='{parsed['conf_name']}' | place='{parsed['conf_place']}' | "
            f"dates='{parsed['conf_dates']}' | order={conf_order}",
        )
        if parsed.get("note"):
            print("NOTE:", parsed["note"])

        if series_slug or stream_iri or series_name:
            print(
                "DBLP:",
                f"slug='{series_slug}' | iri='{stream_iri}' | series='{series_name}'",
            )
            if series_reason:
                print("DBLP_REASON:", series_reason)
        else:
            print("DBLP: no series match")
        # dblp candidates end
        """
        print()
        print()
        print()

        rows.append(
            {
                "pid": pid,
                "name_seq": name_seq,
                "raw_conference": raw,
                "conf_name": parsed["conf_name"],
                "conf_place": parsed["conf_place"],
                "conf_dates": parsed["conf_dates"],
                "conf_begin_date_day": b_day,
                "conf_begin_date_month": b_month,
                "conf_begin_date_year": b_year,
                "conf_end_date_day": e_day,
                "conf_end_date_month": e_month,
                "conf_end_date_year": e_year,
                "conf_order": conf_order,
                "conf_series_slug": series_slug,
                "conf_series_stream_iri": stream_iri,
                "conf_series_name": series_name,
                "conf_series_match_reason": series_reason,
                "note": parsed["note"],
            }
        )

    out = pd.DataFrame(rows)
    print("\nSample of parsed output:")
    print(out.head(20).to_string(index=False))

    write_parsed_table(con, out, "names_conference_parsed")
    out.to_csv("names_conference_parsed_sample.csv", index=False)

    con.close()
    print("\nDone. Wrote parsed data to 'names_conference_parsed' and CSV.")


if __name__ == "__main__":
    main()

