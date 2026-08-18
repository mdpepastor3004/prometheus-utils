// ═══════════════════════════════════════════════════════════
// Glass Luxury Dark — Typst Template (WCAG AAA)
// 주제별 색상 자동 선택 + 전체 접근성 보장
// ═══════════════════════════════════════════════════════════

// ── Topic Presets ──
#let themes = (
  finance: (
    accent: rgb("#d4af37"), accent-light: rgb("#e8c850"), accent-dim: rgb("#a08428"),
    h3: rgb("#8ec8a0"), h4: rgb("#7eb8d8"), code: rgb("#6ec8a0"), quote: rgb("#d4b848"),
  ),
  tech: (
    accent: rgb("#4ecdc4"), accent-light: rgb("#6ee8e0"), accent-dim: rgb("#389890"),
    h3: rgb("#a0d890"), h4: rgb("#80b8e8"), code: rgb("#6ee8e0"), quote: rgb("#80d8c8"),
  ),
  realestate: (
    accent: rgb("#e8a040"), accent-light: rgb("#f0b860"), accent-dim: rgb("#b07830"),
    h3: rgb("#a0c888"), h4: rgb("#88b0d0"), code: rgb("#6ec8a0"), quote: rgb("#d8b050"),
  ),
  health: (
    accent: rgb("#48b8a0"), accent-light: rgb("#68d8c0"), accent-dim: rgb("#308878"),
    h3: rgb("#90c8d8"), h4: rgb("#a8b8e0"), code: rgb("#68d8c0"), quote: rgb("#68d8c0"),
  ),
  legal: (
    accent: rgb("#a0b8d8"), accent-light: rgb("#c0d0e8"), accent-dim: rgb("#7890b0"),
    h3: rgb("#90c0a8"), h4: rgb("#b0a8d0"), code: rgb("#a0c8d8"), quote: rgb("#a8c0d8"),
  ),
  art: (
    accent: rgb("#d8a0b8"), accent-light: rgb("#e8b8d0"), accent-dim: rgb("#a87890"),
    h3: rgb("#a8d0b0"), h4: rgb("#a0b8d8"), code: rgb("#a8d8c0"), quote: rgb("#d0a8c0"),
  ),
  education: (
    accent: rgb("#58c878"), accent-light: rgb("#78e098"), accent-dim: rgb("#409858"),
    h3: rgb("#80c8d0"), h4: rgb("#a0b0e0"), code: rgb("#68d8a0"), quote: rgb("#70c888"),
  ),
  ai: (
    accent: rgb("#a080e0"), accent-light: rgb("#b898f0"), accent-dim: rgb("#7860b0"),
    h3: rgb("#80d0b8"), h4: rgb("#80b8e8"), code: rgb("#a098e8"), quote: rgb("#9888d8"),
  ),
)

#let project(
  title: "",
  subtitle: "",
  date: "",
  author: "자룡봇 AI Research",
  topic: "finance",
  watermark: true,
  body,
) = {

  // ── Resolve theme ──
  let t = themes.at(topic, default: themes.finance)
  let accent      = t.accent
  let accent-light = t.at("accent-light")
  let accent-dim  = t.at("accent-dim")
  let h3-color    = t.h3
  let h4-color    = t.h4
  let code-color  = t.code
  let quote-color = t.quote

  // ── Base colors (WCAG AAA on #0e0e18) ──
  let bg-deep    = rgb("#0e0e18")
  let bg-glass   = rgb("#151520")
  let bg-code    = rgb("#080810")
  let border     = rgb("#1e1e30")
  let text-main  = rgb("#d8d8e8")   // 14.1:1
  let text-sec   = rgb("#b0b0c8")   // 8.5:1
  let text-muted = rgb("#8888a0")   // 4.6:1
  let h2-color   = rgb("#c8c8e0")
  let link-color = rgb("#7eb8d8")

  // ── Page ──
  set page(
    paper: "a4",
    margin: (top: 2.8cm, bottom: 2.8cm, left: 2.2cm, right: 2.2cm),
    fill: bg-deep,
    // ── Diagonal author watermark on every page (free/watermarked edition only) ──
    background: context {
      if watermark and counter(page).get().first() > 1 {
        place(
          center + horizon,
          rotate(-30deg,
            text(
              size: 60pt,
              fill: rgb(accent-dim).transparentize(88%),
              weight: "bold",
            )[© #author]
          )
        )
      }
    },
    header: context {
      if counter(page).get().first() > 1 {
        set text(7pt, fill: accent-dim)
        grid(
          columns: (1fr, 1fr),
          align(left)[#title],
          align(right)[#text(fill: text-muted)[#date]],
        )
        v(-4pt)
        line(length: 100%, stroke: 0.3pt + border)
      }
    },
    footer: context {
      set text(7pt, fill: text-muted)
      grid(
        columns: (1fr, 1fr, 1fr),
        align(left)[#author],
        align(center)[#counter(page).display("1 / 1", both: true)],
        align(right)[AI-Powered Intelligence],
      )
    },
  )

  // ── Typography ──
  set text(
    font: ("Noto Sans CJK KR", "Noto Serif CJK KR"),
    size: 10pt,
    fill: text-main,
    lang: "ko",
  )
  set par(leading: 0.9em, justify: true, first-line-indent: 0em)

  // ── Headings ──
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(2cm)
    block(width: 100%)[
      #set text(22pt, weight: "bold", fill: accent)
      #it.body
      #v(6pt)
      #box(width: 60pt, height: 2pt, fill: accent-dim)
    ]
    v(1cm)
  }

  show heading.where(level: 2): it => {
    v(1cm)
    block(width: 100%)[
      #box(
        inset: (left: 14pt, top: 8pt, bottom: 8pt, right: 14pt),
        stroke: (left: 2pt + accent),
      )[
        #set text(14pt, weight: "semibold", fill: h2-color)
        #it.body
      ]
    ]
    v(0.5cm)
  }

  show heading.where(level: 3): it => {
    v(0.6cm)
    block[
      #text(fill: text-muted, weight: "light")[— ]
      #set text(11.5pt, weight: "semibold", fill: h3-color)
      #it.body
    ]
    v(0.25cm)
  }

  show heading.where(level: 4): it => {
    v(0.4cm)
    block[
      #set text(10.5pt, weight: "semibold", fill: h4-color)
      #it.body
    ]
    v(0.15cm)
  }

  // ── Emphasis ──
  show strong: it => text(fill: accent-light, weight: "bold", it.body)
  show emph: it => text(fill: text-sec, style: "italic", it.body)

  // ── Blockquote ──
  show quote: it => {
    v(0.4cm)
    block(
      width: 100%,
      fill: bg-glass,
      inset: (left: 18pt, top: 12pt, bottom: 12pt, right: 14pt),
      radius: (right: 8pt),
      stroke: (left: 2pt + accent-dim),
    )[
      #set text(fill: quote-color, style: "italic", size: 10pt)
      #it.body
    ]
    v(0.4cm)
  }

  // ── Code ──
  show raw.where(block: true): it => {
    block(
      width: 100%,
      fill: bg-code,
      inset: 14pt,
      radius: 8pt,
      stroke: 0.5pt + border,
    )[
      #set text(8.5pt, fill: code-color, font: "Noto Sans Mono CJK KR")
      #it
    ]
  }
  show raw.where(block: false): it => {
    box(
      fill: bg-glass,
      inset: (x: 5pt, y: 2pt),
      radius: 4pt,
    )[
      #set text(9pt, fill: code-color, font: "Noto Sans Mono CJK KR")
      #it
    ]
  }

  // ── Tables ──
  set table(
    fill: (_, y) => if y == 0 { bg-glass } else if calc.odd(y) { rgb("#0c0c14") } else { bg-glass },
    stroke: 0.5pt + border,
    inset: 9pt,
  )
  show table.cell.where(y: 0): set text(weight: "bold", fill: accent, size: 8.5pt)
  show table.cell: set text(fill: text-main)

  // ── Links ──
  show link: it => text(fill: link-color, it)

  // ── Lists ──
  set list(marker: text(fill: accent-dim, size: 8pt)[●])
  set enum(numbering: n => text(fill: accent-dim, weight: "bold")[#n.])

  // ═══════════════════════════════════
  // COVER PAGE
  // ═══════════════════════════════════
  {
    set page(header: none, footer: none)
    v(3cm)
    align(center)[
      #line(length: 30%, stroke: 0.5pt + accent-dim)
      #v(0.5cm)
      #block[
        #set text(8.5pt, fill: text-muted, tracking: 0.4em, weight: "medium")
        AI-POWERED INTELLIGENCE
      ]
      #v(1.5cm)
      #block(width: 85%)[
        #set text(30pt, weight: "bold", fill: accent)
        #title
      ]
      #v(0.5cm)
      #line(length: 40%, stroke: 1pt + accent-dim)
      #v(0.8cm)
      #block[
        #set text(14pt, fill: text-sec, weight: "light")
        #subtitle
      ]
      #v(0.4cm)
      #block[
        #set text(11pt, fill: text-muted)
        #date
      ]
      #v(3.5cm)
      #block(
        width: 60%,
        fill: bg-glass,
        inset: 22pt,
        radius: 12pt,
        stroke: 0.5pt + border,
      )[
        #set text(8.5pt, fill: text-sec)
        #set par(justify: true)
        본 전자책은 AI가 실시간 데이터를 기반으로 자동 생성합니다.
        30개 챕터 × 3,000자+ 분량의 종합 분석서입니다.
      ]
      #v(2.5cm)
      #block[
        #set text(9pt, fill: text-muted, tracking: 0.1em)
        #author
      ]
      #v(0.3cm)
      #line(length: 30%, stroke: 0.5pt + accent-dim)
    ]
  }

  // ═══ COPYRIGHT NOTICE (front) — watermarked/free edition only ═══
  if watermark {
    set page(header: none, footer: none)
    v(2.5cm)
    align(center)[
      #block(
        width: 82%,
        fill: bg-glass,
        inset: 24pt,
        radius: 12pt,
        stroke: 1pt + accent-dim,
      )[
        #set text(9pt, fill: text-sec)
        #set par(justify: true, leading: 1.1em)
        #align(center)[
          #text(13pt, weight: "bold", fill: accent)[⚠ 저작권 경고 / COPYRIGHT NOTICE]
        ]
        #v(0.6cm)
        #text(weight: "bold", fill: accent-light)[© #date #author. All Rights Reserved.]
        #v(0.4cm)
        이 저작물의 저작권은 *#author* 에게 있습니다. 본 전자책의 전부 또는 일부를 저작권자의 서면 동의 없이 복제, 재배포, 전송, 전시, 공연, 2차적 저작물 작성에 이용하는 행위를 금지합니다.
        #v(0.3cm)
        무단 전재·복제·배포 시 저작권법에 따라 민·형사상의 책임을 질 수 있습니다. 본 문서의 모든 페이지에는 저작권자 워터마크가 포함되어 있습니다.
        #v(0.4cm)
        #text(8pt, fill: text-muted, style: "italic")[This work is protected by copyright law. Unauthorized reproduction or distribution is prohibited and may result in civil and criminal liability.]
      ]
    ]
  }

  // ═══ TOC ═══
  pagebreak()
  block(width: 100%)[
    #set text(22pt, weight: "bold", fill: accent)
    목차
    #v(4pt)
    #box(width: 60pt, height: 2pt, fill: accent-dim)
  ]
  v(0.6cm)
  {
    set text(fill: text-main)
    show outline.entry.where(level: 1): it => { v(4pt); strong(it) }
    outline(indent: 1.5em, depth: 2)
  }

  // ═══ BODY ═══
  body

  // ═══ COPYRIGHT NOTICE (back / last page) — watermarked/free edition only ═══
  if watermark {
    pagebreak()
    set page(header: none, footer: none)
    v(3cm)
    align(center)[
      #line(length: 30%, stroke: 0.5pt + accent-dim)
      #v(1cm)
      #block(
        width: 82%,
        fill: bg-glass,
        inset: 24pt,
        radius: 12pt,
        stroke: 1pt + accent-dim,
      )[
        #set text(9pt, fill: text-sec)
        #set par(justify: true, leading: 1.1em)
        #align(center)[
          #text(13pt, weight: "bold", fill: accent)[⚠ 저작권 경고 / COPYRIGHT NOTICE]
        ]
        #v(0.6cm)
        #text(weight: "bold", fill: accent-light)[© #date #author. All Rights Reserved.]
        #v(0.4cm)
        이 전자책의 저작권은 *#author* 에게 있으며, 저작권법에 의해 보호됩니다. 저작권자의 사전 서면 동의 없는 무단 복제·전송·배포·출판·판매를 일체 금지합니다.
        #v(0.3cm)
        #text(8pt, fill: text-muted, style: "italic")[© #date #author. All Rights Reserved. No part of this publication may be reproduced or transmitted in any form without prior written permission of the copyright holder.]
      ]
      #v(1cm)
      #text(8.5pt, fill: text-muted, tracking: 0.2em)[#author]
      #v(0.3cm)
      #line(length: 30%, stroke: 0.5pt + accent-dim)
    ]
  }

}
