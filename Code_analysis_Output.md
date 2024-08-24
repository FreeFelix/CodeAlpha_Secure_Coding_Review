Run started:2024-08-24 11:35:12.971322

Test results:
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b608_hardcoded_sql_expressions.html
   Location: ./file.py:13:19
12	    cursor = conn.cursor()
13	    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
14	    conn.commit()

--------------------------------------------------
>> Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
   Severity: High   Confidence: Medium
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b201_flask_debug_true.html
   Location: ./file.py:20:4
19	if __name__ == '__main__':
20	    app.run(debug=True)

--------------------------------------------------
>> Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
   Severity: High   Confidence: Medium
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b201_flask_debug_true.html
   Location: ./file2.py:34:4
33	if __name__ == '__main__':
34	    app.run(debug=True)

--------------------------------------------------

Code scanned:
	Total lines of code: 41
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 1
		High: 2
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 3
		High: 0
Files skipped (0):
