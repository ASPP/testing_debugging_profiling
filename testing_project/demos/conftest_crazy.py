# conftest.py
import pytest
import random

import numpy as np
import pytest


# add a commandline option to pytest
def pytest_addoption(parser):
    """Add random seed option to py.test.
    """
    parser.addoption('--seed', dest='seed', type=int, action='store',
                     help='set random seed')


# configure pytest to automatically set the rnd seed if not passed on CLI
def pytest_configure(config):
    seed = config.getvalue("seed")
    # if seed was not set by the user, we set one now
    if seed is None or seed == ('NO', 'DEFAULT'):
        config.option.seed = int(np.random.randint(2 ** 31 - 1))


def pytest_report_header(config):
    return f'Using random seed: {config.option.seed}'


@pytest.fixture
def random_state(request):
    random_state = np.random.RandomState(request.config.option.seed)
    return random_state


# conftest.py
import pytest
import random

FLASHY_EMOJIS_PASS = ["🎉", "✨", "🌈", "💎", "🔥", "🚀", "💃", "🍾", "🥳"]
FLASHY_EMOJIS_FAIL = ["💀", "🔥", "💔", "😱", "👹", "🩸", "☠️", "👾", "🤯"]
FLASHY_EMOJIS_SKIP = ["⏭", "🙃", "🕊", "💤", "📭", "🤸"]

# Vivid ANSI 256-color palette (high contrast, no pale shades)
VIVID_COLORS = [196, 202, 208, 34, 27, 93, 129, 201]  
# bright red, orange, gold, green, deep blue, violet, magenta, pink

def rainbow_text(text: str) -> str:
    """Return text with vivid rainbow cycling ANSI 256-color codes."""
    result = []
    for i, char in enumerate(text):
        color = VIVID_COLORS[i % len(VIVID_COLORS)]
        result.append(f"\033[38;5;{color}m{char}\033[0m")
    return "".join(result)

def big_banner(text: str) -> str:
    """ASCII art style banner with rainbow colors."""
    border = rainbow_text("=" * (len(text) + 12))
    middle = rainbow_text(f"🌟✨ {text} ✨🌟")
    return f"\n{border}\n{middle}\n{border}\n"

def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.failed:
            return report.outcome, "💥", "FAILED FLASHY"
        elif report.passed:
            return report.outcome, "🌟", "PASSED FLASHY"
        elif report.skipped:
            return report.outcome, "⏭", "SKIPPED FLASHY"

@pytest.hookimpl(trylast=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    total = terminalreporter._numcollected
    failed = len(terminalreporter.stats.get("failed", []))
    passed = len(terminalreporter.stats.get("passed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))

    # Rainbow banner
    print(big_banner("PYTEST PARTY REPORT"))

    if passed:
        emoji = random.choice(FLASHY_EMOJIS_PASS)
        print(rainbow_text(f"{emoji} {passed} TESTS PASSED {emoji}"))
    if failed:
        emoji = random.choice(FLASHY_EMOJIS_FAIL)
        print(rainbow_text(f"{emoji} {failed} TESTS FAILED {emoji}"))
    if skipped:
        emoji = random.choice(FLASHY_EMOJIS_SKIP)
        print(rainbow_text(f"{emoji} {skipped} TESTS SKIPPED {emoji}"))

    print(big_banner(f"TOTAL: {total}"))
    print(rainbow_text("🎆🎇✨ PYTEST PARTY OVER ✨🎇🎆"))



# # Only include colors supported by TerminalWriter.markup
# FLASHY_COLORS = ["red", "green", "yellow", "blue", "cyan", "white"]

# FLASHY_EMOJIS_PASS = ["🎉", "✨", "🌈", "💎", "🔥", "🚀", "💃"]
# FLASHY_EMOJIS_FAIL = ["💀", "🔥", "💔", "😱", "👹", "🩸", "☠️"]
# FLASHY_EMOJIS_SKIP = ["⏭", "🙃", "🕊", "💤", "📭"]




# def random_style(tw, text: str, emojis: list) -> str:
#     """Return text wrapped in random color and emoji bling."""
#     color = random.choice(FLASHY_COLORS)
#     emoji = random.choice(emojis)
#     kwargs = {"bold": True, color: True}
#     return tw.markup(f"{emoji} {text} {emoji}", **kwargs)


# def pytest_report_teststatus(report, config):
#     """Customize symbols in the progress line (dots → flashy)."""
#     if report.when == "call":
#         if report.failed:
#             return report.outcome, "💥", "FAILED FLASHY"
#         elif report.passed:
#             return report.outcome, "🌟", "PASSED FLASHY"
#         elif report.skipped:
#             return report.outcome, "⏭", "SKIPPED FLASHY"


# @pytest.hookimpl(trylast=True)
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     tw = terminalreporter._tw
#     total = terminalreporter._numcollected

#     failed = len(terminalreporter.stats.get("failed", []))
#     passed = len(terminalreporter.stats.get("passed", []))
#     skipped = len(terminalreporter.stats.get("skipped", []))

#     tw.sep("=", random_style(tw, "🌟🌟 TEST SUMMARY 🌟🌟", FLASHY_EMOJIS_PASS))

#     if passed:
#         tw.write(random_style(tw, f"{passed} TESTS PASSED", FLASHY_EMOJIS_PASS) + "\n")
#     if failed:
#         tw.write(random_style(tw, f"{failed} TESTS FAILED", FLASHY_EMOJIS_FAIL) + "\n")
#     if skipped:
#         tw.write(random_style(tw, f"{skipped} TESTS SKIPPED", FLASHY_EMOJIS_SKIP) + "\n")

#     tw.sep("=", random_style(tw, f"TOTAL: {total}", FLASHY_EMOJIS_PASS))
#     tw.write("\n")
#     tw.write(random_style(tw, "✨ PYTEST PARTY OVER ✨", FLASHY_EMOJIS_PASS) + "\n")
