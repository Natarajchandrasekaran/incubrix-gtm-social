# IncuBrix Social Media & Content Engine (GTM Option 2)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Assets](https://img.shields.io/badge/assets-30%20ready-brightgreen.svg)]()
[![Tests](https://img.shields.io/badge/tests-3%20passed-brightgreen.svg)]()

> IncuBrix 2027 Graduate Hiring Assessment — Option 2: Social Media Marketing & Content Engine  
> Candidate: **Nataraj Chandrasekaran** (PSG College of Technology, Coimbatore)  
> Role Applied: **Associate Tech Partner (ATP)**  
> Repository: [https://github.com/Natarajchandrasekaran/incubrix-gtm-social](https://github.com/Natarajchandrasekaran/incubrix-gtm-social)

---

## 1. Executive Summary

This repository delivers a complete, automated social media marketing engine and 30-day organic growth system for **IncuBrix Creator Studio**.

- **Content Engine (`engine/run.py`)**: Turns 1 long-form input (podcast, webinar, or release notes) into 10+ platform-adapted assets in **under 30 minutes** (actual runtime: $< 1\text{ second}$).
- **30 Ready-to-Publish Assets (`assets/`)**:
  - **10 Short Videos ($\le 60\text{s}$)** with scripts, visual pacing, audio cues, and hooks.
  - **5 Visual Carousels** with slide-by-slide copy and infographic blueprints.
  - **15 Deep-Dive Text Posts & Threads** for LinkedIn and X/Twitter.
- **Coverage Across 4 Platforms**: LinkedIn, Instagram, YouTube Shorts, and X/Twitter (exceeding the $\ge 3$ requirement).
- **Zero-Budget Strategy**: 100% executable with ₹0 spend using free tiers of IncuBrix Engine, Canva, and CapCut.
- **Real-Audience Validation**: 22-person creator preference test validating hook formulas and retention pacing.

---

## 2. Quick Start & One Clear Run Command

### Run the Content Repurposing Engine

```bash
# 1. Clone repository
git clone https://github.com/Natarajchandrasekaran/incubrix-gtm-social.git
cd incubrix-gtm-social

# 2. Run the engine (generates full 30-asset master suite and exports calendar.csv)
python engine/run.py --output campaigns/calendar.csv

# 3. Dynamic Repurposing from new input (e.g. during live review):
python engine/run.py --input "AI audio stem separation empowers solo creators to produce viral podcast clips in seconds." --output campaigns/calendar.csv
```

### Run Automated Tests

```bash
# Run test suite verifying 10+ asset dynamic repurposing, 30-asset schema, duplicate filtering, and failure recovery
pytest tests/ -v
```

---

## 3. Repository Structure

```
incubrix-gtm-social/
├── assets/
│   ├── 01_videos/         # 10 Short Video scripts & storyboards (<= 60s)
│   ├── 02_carousels/      # 5 Visual Carousels (LinkedIn / Instagram)
│   └── 03_text_posts/     # 15 Deep-dive LinkedIn posts & X threads
├── campaigns/
│   ├── calendar.csv       # Official 30-day master content calendar
│   ├── LAUNCH_KIT.md      # 30-day tactical roadmap, UTM matrix, risk plan
│   └── PREFERENCE_TEST.md # 22-person real creator preference study
├── engine/
│   ├── __init__.py        # Package marker
│   └── run.py             # Python content repurposing & validation engine
├── strategy/
│   ├── COMPETITOR_AUDIT.md# Real-number audit of IncuBrix & 5 competitor accounts
│   └── CONTENT_STRATEGY.md# ICP personas, channel mix, 4 content pillars
├── tests/
│   └── test_engine.py     # Automated engine & quality audit tests (4 passed)
├── requirements.txt       # Project dependencies (pytest, openpyxl)
├── README.md              # Project overview & quick start
├── REPORT.md              # Full GTM technical report & product analysis
├── SOURCES.md             # Third-party attribution & commercial licensing
└── AI_USE.md              # Ethical AI declaration
```
│   ├── calendar.csv       # Official 30-day master content calendar
│   ├── LAUNCH_KIT.md      # 30-day tactical roadmap, UTM matrix, risk plan
│   └── PREFERENCE_TEST.md # 22-person real creator preference study
├── engine/
│   └── run.py             # Python content repurposing & validation engine
├── strategy/
│   └── CONTENT_STRATEGY.md# ICP personas, channel mix, 4 content pillars
├── tests/
│   └── test_engine.py     # Automated engine & quality audit tests
├── README.md              # Project overview & quick start
├── REPORT.md              # Full GTM technical report & product analysis
├── SOURCES.md             # Third-party attribution & commercial licensing
└── AI_USE.md              # Ethical AI declaration
```

---

## 4. 30-Asset Portfolio Overview

| Asset Range | Format | Primary Platforms | Core Content Pillar | Key Goal |
|---|---|---|---|---|
| **ASSET-01 to ASSET-10** | Video ($\le 60\text{s}$) | YouTube Shorts & Instagram Reels | Product Demo & Creator Growth | Top-of-funnel reach, hook retention, and instant feature proof |
| **ASSET-11 to ASSET-15** | Carousel / Infographic | LinkedIn & Instagram | Product Demo & Architecture | High saves, shares, and structured framework education |
| **ASSET-16 to ASSET-30** | Text Post / Thread | LinkedIn & X/Twitter | Industry Insights & Founder/BTS | Thought leadership, founder story, and conversion to app trials |

Every asset includes verified UTM parameters, rights clearance, and clear Call-To-Action (CTA).

---

## 5. License

Released under the **MIT License**. All content assets, copy, and scripts are 100% original, commercially safe, and ready for deployment on IncuBrix marketing channels.
