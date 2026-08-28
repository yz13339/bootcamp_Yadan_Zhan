# Outlier assumptions

Daily returns outside 1.5 IQR fences are flagged, never silently deleted. Market extremes can be genuine stress signals, so the primary model retains them; a 1%/99% winsorized scenario measures sensitivity. Removing genuine crises would understate portfolio risk, while retaining bad source values could exaggerate it. Flagged dates require source verification before operational use.
