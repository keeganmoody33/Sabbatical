.PHONY: run check views quality list

# The default. Runs every stage and fails if a re-run of a frozen corpus moved
# an existing output.
check:
	python3 pipeline/run.py

# Same stages, permitting intended changes. An intended change must also be
# logged in the knowledge/protocol.md changelog and disclosed in paper/DEFECTS.md.
run:
	python3 pipeline/run.py --write

list:
	python3 pipeline/run.py --list

# The two view-layer stages on their own, for iterating on an analysis without
# re-running adjudication.
views:
	python3 pipeline/build_views.py

quality:
	python3 pipeline/data_quality.py
