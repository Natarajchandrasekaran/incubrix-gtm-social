"""
Tests for IncuBrix Social Media Content Engine.
Assessment 2 (GTM Option 2).
"""
from __future__ import annotations

import csv
import tempfile
import time
from pathlib import Path

import pytest
from engine.run import ContentEngine, RAW_30_ASSETS, generate_all_30_assets


def test_engine_repurpose_single_input():
    """Verify engine generates 10+ assets in under 30 minutes."""
    sample_text = (
        "IncuBrix Creator Studio empowers solopreneurs and founders to repurpose long video into 10 viral clips. "
        "With text-based video editing, voice cloning, auto-captions, and multi-channel publishing to YouTube, "
        "Instagram, LinkedIn, and Bluesky, creators save 15+ hours weekly on manual editing."
    )
    engine = ContentEngine()
    with tempfile.TemporaryDirectory() as tmpdir:
        out_csv = Path(tmpdir) / "calendar.csv"
        assets_dir = Path(tmpdir) / "assets"
        start = time.time()
        assets = engine.run_repurpose(sample_text, "Test Transcript", out_csv, assets_dir)
        elapsed = time.time() - start

        # Must generate 10+ assets in < 30 minutes (1800s)
        assert len(assets) >= 10
        assert elapsed < 1800.0
        assert out_csv.exists()


def test_full_30_assets_suite():
    """Verify complete suite of 30 assets complies with brief criteria."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_csv = Path(tmpdir) / "calendar.csv"
        base_dir = Path(tmpdir)
        assets = generate_all_30_assets(out_csv, base_dir)

        assert len(assets) == 30

        # Check format breakdown
        videos = [a for a in assets if "video" in a.format.lower()]
        carousels = [a for a in assets if "carousel" in a.format.lower()]
        text_posts = [a for a in assets if "text" in a.format.lower() or "thread" in a.format.lower()]

        assert len(videos) >= 10, f"Expected >= 10 videos, got {len(videos)}"
        assert len(carousels) >= 5, f"Expected >= 5 carousels, got {len(carousels)}"
        assert len(text_posts) >= 15, f"Expected >= 15 text posts, got {len(text_posts)}"

        # Check platforms (minimum 3 required)
        platforms = {a.platform for a in assets}
        assert len(platforms) >= 3

        # Check UTM links
        for a in assets:
            assert "utm_source=" in a.utm_link
            assert "utm_medium=social" in a.utm_link
            assert "utm_campaign=" in a.utm_link

        # Check quality
        for a in assets:
            assert len(a.hook.strip()) >= 10
            assert len(a.caption.strip()) >= 30
            assert a.cta != ""
            assert a.rights_checked == "Yes"


def test_duplicate_detection():
    """Verify duplicate detection identifies replayed text."""
    engine = ContentEngine()
    fp1 = engine.generate_fingerprint("Why 90% of your Shorts get stuck at 400 views")
    fp2 = engine.generate_fingerprint("Why 90% of your Shorts get stuck at 400 views!")
    # Normalized fingerprinting ignores punctuation and case
    assert fp1 == fp2


def test_failure_and_recovery_empty_input():
    """Verify engine handles malformed or empty inputs gracefully without crashing."""
    engine = ContentEngine()
    with tempfile.TemporaryDirectory() as tmpdir:
        out_csv = Path(tmpdir) / "calendar.csv"
        assets_dir = Path(tmpdir) / "assets"

        # Empty string input
        res1 = engine.run_repurpose("", "Empty Input", out_csv, assets_dir)
        assert len(res1) == 0

        # Sub-minimum length input (5 characters)
        res2 = engine.run_repurpose("Short", "5 Chars", out_csv, assets_dir)
        assert len(res2) == 0

