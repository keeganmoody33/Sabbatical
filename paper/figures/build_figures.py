"""Build freeze figures as SVG. Series come from census CSVs, not from captions."""

from __future__ import annotations

import html
from pathlib import Path

from series import LANE_LABEL, LANE_ORDER, MONTH_LABEL, MONTHS, assert_freeze_headlines, compute

OUT = Path(__file__).resolve().parent
INK = "#1c1917"
MUTED = "#57534e"
BAR = "#1e3a5f"
BAR2 = "#7a93b0"
INTERVIEW = "#6b2d3c"
LIGHT = "#e7e5e4"
PAPER = "#faf8f5"


def esc(text: object) -> str:
    return html.escape(str(text), quote=True)


def svg_wrap(width: int, height: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">\n'
        f'<rect width="{width}" height="{height}" fill="{PAPER}"/>\n'
        f"{body}\n</svg>\n"
    )


def text(x: float, y: float, content: object, *, size: int = 12, fill: str = INK, anchor: str = "start", weight: str = "normal") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Georgia, \'Times New Roman\', serif" '
        f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">'
        f"{esc(content)}</text>"
    )


def vertical_bars(
    *,
    series_a: list[int],
    labels: list[str],
    note: str,
    path: Path,
    series_b: list[int] | None = None,
    legend: tuple[str, str] | None = None,
    ymax: int | None = None,
) -> None:
    width, height = 920, 420
    left, right, top, bottom = 56, 24, 28, 78
    plot_w = width - left - right
    plot_h = height - top - bottom
    n = len(series_a)
    totals = [a + (series_b[i] if series_b else 0) for i, a in enumerate(series_a)]
    ymax = ymax or max(totals + [1])
    ymax = max(35, ((ymax + 4) // 5) * 5)
    gap = 6
    bar_w = (plot_w / n) - gap
    parts = [text(left, 20, note, size=12, fill=MUTED)]
    for tick in range(0, ymax + 1, 5):
        y = top + plot_h - (tick / ymax) * plot_h
        parts.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}" '
            f'stroke="{LIGHT}" stroke-width="1"/>'
        )
        parts.append(text(left - 8, y + 4, tick, size=11, fill=MUTED, anchor="end"))
    for i, (label, a) in enumerate(zip(labels, series_a)):
        x = left + i * (bar_w + gap) + gap / 2
        h_a = (a / ymax) * plot_h
        y_a = top + plot_h - h_a
        parts.append(
            f'<rect x="{x:.1f}" y="{y_a:.1f}" width="{bar_w:.1f}" height="{h_a:.1f}" fill="{BAR}"/>'
        )
        if series_b:
            b = series_b[i]
            h_b = (b / ymax) * plot_h
            y_b = y_a - h_b
            parts.append(
                f'<rect x="{x:.1f}" y="{y_b:.1f}" width="{bar_w:.1f}" height="{h_b:.1f}" fill="{BAR2}"/>'
            )
        total = totals[i]
        if total:
            y_label = top + plot_h - (total / ymax) * plot_h - 4
            parts.append(text(x + bar_w / 2, y_label, total, size=10, fill=INK, anchor="middle"))
        parts.append(
            text(x + bar_w / 2, height - 44, label.split(" ")[0], size=10, fill=MUTED, anchor="middle")
        )
        parts.append(
            text(x + bar_w / 2, height - 30, label.split(" ")[1], size=10, fill=MUTED, anchor="middle")
        )
    if legend:
        parts.append(f'<rect x="{left}" y="{height - 22}" width="12" height="12" fill="{BAR}"/>')
        parts.append(text(left + 18, height - 12, legend[0], size=11, fill=MUTED))
        if series_b:
            parts.append(f'<rect x="{left + 210}" y="{height - 22}" width="12" height="12" fill="{BAR2}"/>')
            parts.append(text(left + 228, height - 12, legend[1], size=11, fill=MUTED))
    path.write_text(svg_wrap(width, height, "\n".join(parts)), encoding="utf-8")


def fig3(data: dict[str, object]) -> None:
    width, height = 880, 420
    left, right, top, bottom = 150, 36, 28, 36
    plot_w = width - left - right
    plot_h = height - top - bottom
    n = len(LANE_ORDER)
    row_h = plot_h / n
    xmax = 120
    parts = [
        text(left, 20, "Freeze 1 n = 221 (kappa 0.9510). Full census n = 298. No second kappa on the 77.", size=12, fill=MUTED)
    ]
    freeze1 = data["lane_freeze1"]
    full = data["lane_full"]
    for i, lane in enumerate(LANE_ORDER):
        y = top + i * row_h + 10
        a = freeze1[lane]
        b = full[lane]
        parts.append(text(left - 8, y + 14, LANE_LABEL[lane], size=12, fill=INK, anchor="end"))
        w_a = (a / xmax) * (plot_w - 8)
        w_b = (b / xmax) * (plot_w - 8)
        parts.append(f'<rect x="{left}" y="{y:.1f}" width="{w_b:.1f}" height="10" fill="{BAR2}"/>')
        parts.append(f'<rect x="{left}" y="{y + 12:.1f}" width="{w_a:.1f}" height="10" fill="{BAR}"/>')
        parts.append(text(left + w_b + 6, y + 9, f"{b}", size=11, fill=MUTED))
        parts.append(text(left + w_a + 6, y + 21, f"{a}", size=11, fill=INK))
    parts.append(f'<rect x="{left}" y="{height - 22}" width="12" height="12" fill="{BAR}"/>')
    parts.append(text(left + 18, height - 12, "Freeze 1 (221)", size=11, fill=MUTED))
    parts.append(f'<rect x="{left + 160}" y="{height - 22}" width="12" height="12" fill="{BAR2}"/>')
    parts.append(text(left + 178, height - 12, "full census (298)", size=11, fill=MUTED))
    OUT.joinpath("fig-03-role-lane.svg").write_text(svg_wrap(width, height, "\n".join(parts)), encoding="utf-8")


def fig4() -> None:
    width, height = 760, 360
    parts = [
        text(40, 24, "Interviewed is derived. The 77 Freeze 2 rows add volume, not interview-set events.", size=12, fill=MUTED)
    ]
    columns = [
        ("Freeze 1", 14, 221, 80),
        ("full census", 14, 298, 320),
        ("employer artifact", 14, 220, 560),
    ]
    max_h = 220
    for label, num, den, x in columns:
        h_iv = (num / den) * max_h
        h_rest = max_h - h_iv
        y0 = 50
        parts.append(f'<rect x="{x}" y="{y0}" width="120" height="{h_rest:.1f}" fill="{LIGHT}"/>')
        parts.append(
            f'<rect x="{x}" y="{y0 + h_rest:.1f}" width="120" height="{h_iv:.1f}" fill="{INTERVIEW}"/>'
        )
        parts.append(text(x + 60, y0 + 28, f"{den - num} not interviewed", size=11, fill=MUTED, anchor="middle"))
        parts.append(text(x + 60, y0 + max_h + 22, f"{num}/{den}", size=16, fill=INK, anchor="middle", weight="bold"))
        parts.append(text(x + 60, y0 + max_h + 42, label, size=12, fill=MUTED, anchor="middle"))
    parts.append(f'<rect x="40" y="{height - 28}" width="12" height="12" fill="{INTERVIEW}"/>')
    parts.append(text(62, height - 18, "interviewed (14)", size=11, fill=MUTED))
    parts.append(f'<rect x="220" y="{height - 28}" width="12" height="12" fill="{LIGHT}"/>')
    parts.append(text(242, height - 18, "not interviewed", size=11, fill=MUTED))
    OUT.joinpath("fig-04-two-denominators.svg").write_text(svg_wrap(width, height, "\n".join(parts)), encoding="utf-8")


def fig5(data: dict[str, object]) -> None:
    width, height = 820, 280
    outcomes = [
        ("still_open", "still open", data["outcomes_freeze1"]["still_open"]),
        ("rejected_no_interview", "rejected, no interview", data["outcomes_freeze1"]["rejected_no_interview"]),
        ("role_paused_or_closed", "role paused or closed", data["outcomes_freeze1"]["role_paused_or_closed"]),
        ("rejected_after_interview", "rejected after interview", data["outcomes_freeze1"]["rejected_after_interview"]),
    ]
    xmax = 221
    left = 220
    parts = [
        text(40, 22, "Freeze 1 only (n = 221). The 77 platform rows are blank and are not in this figure.", size=12, fill=MUTED)
    ]
    for i, (_key, label, n) in enumerate(outcomes):
        y = 48 + i * 48
        w = (n / xmax) * 520
        parts.append(text(left - 12, y + 16, label, size=13, fill=INK, anchor="end"))
        parts.append(f'<rect x="{left}" y="{y}" width="{w:.1f}" height="22" fill="{BAR if i else MUTED}"/>')
        parts.append(text(left + w + 8, y + 16, f"{n}/221", size=13, fill=INK))
    OUT.joinpath("fig-05-freeze1-outcomes.svg").write_text(svg_wrap(width, height, "\n".join(parts)), encoding="utf-8")


def fig6() -> None:
    width, height = 880, 320
    boxes = [
        (40, 40, "A. Application census", "298 applications", "14 interviewed", "rate 14/298"),
        (460, 40, "B. Opportunity", "outside the 14", "not added to the rate", "overlay tagged memory"),
        (40, 170, "C. Money", "listed beside the rate", "marketplace rows sit in A", "without conversion"),
        (460, 170, "D. Communal", "not jobs", "not a pipeline", "not a rate"),
    ]
    parts = [
        text(40, 24, "Four boards. Do not stack B into A. Naming pass still required for paid names in C.", size=12, fill=MUTED)
    ]
    for x, y, title, l1, l2, l3 in boxes:
        parts.append(f'<rect x="{x}" y="{y}" width="380" height="110" fill="#fff" stroke="{BAR}" stroke-width="1.5"/>')
        parts.append(text(x + 16, y + 28, title, size=15, fill=INK, weight="bold"))
        parts.append(text(x + 16, y + 52, l1, size=13, fill=MUTED))
        parts.append(text(x + 16, y + 72, l2, size=13, fill=MUTED))
        parts.append(text(x + 16, y + 92, l3, size=13, fill=MUTED))
    OUT.joinpath("fig-06-scoreboards.svg").write_text(svg_wrap(width, height, "\n".join(parts)), encoding="utf-8")


def fig7(data: dict[str, object]) -> None:
    order = [
        ("plain", "plain"),
        ("founding_senior_lead", "founding/senior/lead"),
        ("systems_operations", "systems/operations"),
        ("ai_product_vertical", "AI/product/vertical"),
        ("sales_presales", "sales/presales"),
        ("growth_marketing", "growth/marketing"),
    ]
    freeze1 = data["gtm_modifier_freeze1"]
    full = data["gtm_modifier_full"]
    width, height = 880, 340
    left = 200
    parts = [
        text(40, 22, "Explicit GTM only. Freeze 1 n = 86. Full census n = 113. Not a second kappa.", size=12, fill=MUTED)
    ]
    xmax = 80
    for i, (key, label) in enumerate(order):
        y = 44 + i * 42
        a = freeze1.get(key, 0)
        b = full.get(key, 0)
        parts.append(text(left - 12, y + 16, label, size=13, fill=INK, anchor="end"))
        parts.append(f'<rect x="{left}" y="{y}" width="{(b / xmax) * 520:.1f}" height="10" fill="{BAR2}"/>')
        parts.append(f'<rect x="{left}" y="{y + 12}" width="{(a / xmax) * 520:.1f}" height="10" fill="{BAR}"/>')
        parts.append(text(left + (b / xmax) * 520 + 6, y + 10, str(b), size=11, fill=MUTED))
        parts.append(text(left + (a / xmax) * 520 + 6, y + 22, str(a), size=11, fill=INK))
    parts.append(f'<rect x="{left}" y="{height - 24}" width="12" height="12" fill="{BAR}"/>')
    parts.append(text(left + 18, height - 14, "Freeze 1 GTM (86)", size=11, fill=MUTED))
    parts.append(f'<rect x="{left + 180}" y="{height - 24}" width="12" height="12" fill="{BAR2}"/>')
    parts.append(text(left + 198, height - 14, "full GTM (113)", size=11, fill=MUTED))
    OUT.joinpath("fig-07-gtm-modifiers.svg").write_text(svg_wrap(width, height, "\n".join(parts)), encoding="utf-8")


def main() -> None:
    data = compute()
    assert_freeze_headlines(data)
    labels = [MONTH_LABEL[month] for month in MONTHS]
    freeze1 = [data["monthly_freeze1"][month] for month in MONTHS]
    full = [data["monthly_full"][month] for month in MONTHS]
    increment = [b - a for a, b in zip(freeze1, full)]
    vertical_bars(
        series_a=freeze1,
        labels=labels,
        note="Freeze 1 exact dates only. n exact = 195. n not exact = 26, not plotted. Sep/Oct 2025 zero is not zero activity.",
        path=OUT / "fig-01-monthly-freeze1.svg",
    )
    vertical_bars(
        series_a=freeze1,
        series_b=increment,
        labels=labels,
        note="Full census exact dates. n exact = 201. 71 LinkedIn relative stamps are off-chart. Peak Jul 2026 remains 33.",
        path=OUT / "fig-02-monthly-full.svg",
        legend=("Freeze 1 exact", "Freeze 2 exact Jobright add"),
    )
    fig3(data)
    fig4()
    fig5(data)
    fig6()
    fig7(data)
    print("wrote 7 SVGs under paper/figures/")


if __name__ == "__main__":
    main()
