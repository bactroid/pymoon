#!/usr/bin/python
"""Functions for calculating moon phase."""

import datetime
import math


def getMoonPhase(date):
    """
    Get decimal moon phase for a date.

    Date should be in the format YYYY-MM-DD.
    Moon phase will be a decimal number between 0 and 1 where...
    0,1 = New moon
    0.5 = Full Moon

    Algorithm influenced by Ben Daglish:
    http://www.ben-daglish.net/moon.shtml
    """
    phase_len = 2551443
    year, month, day = date.split("-", 2)
    epoch = datetime.datetime(1970, 1, 1)
    new_moon = (datetime.datetime(1970, 1, 7) - epoch).total_seconds()
    user_date = (datetime.datetime(int(year), int(month), int(day)) -
                 epoch).total_seconds()
    phase = (user_date - new_moon) % phase_len
    return math.floor(phase / (24 * 3600) + 1)


def interpretMoonPhase(phase):
    """
    Translate phase into common language for moon phases.
    """
    if phase == 0 or phase == 30:
        return "New Moon"
    if phase > 0 and phase < 7.5:
        return "Waxing Crescent"
    if phase > 7.5 and phase < 15:
        return "Waxing Gibbous"
    if phase == 15:
        return "Full Moon"
    if phase > 15 and phase < 22.5:
        return "Waning Gibbous"
    if phase > 22.5 and phase < 30:
        return "Waning Crescent"


def main():
    user_date = "2015-12-25"
    phase = getMoonPhase(user_date)
    print (user_date + ": " + interpretMoonPhase(phase) + " (" + str(phase) +
           " days into cycle)")

if __name__ == "__main__":
    main()
