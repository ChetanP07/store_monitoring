from flask import Flask, request, jsonify
import uuid
import threading
import time
from report import generate_store_report

app = Flask(__name__)

# API endpoint to trigger report generation
@app.route('/trigger_report', methods=['POST'])
def trigger_report():
    report_id = str(uuid.uuid4())
    return jsonify({"report_id": report_id})

# API endpoint to get the status of the report
@app.route('/get_report', methods=['GET'])
def get_report():
    report_id = request.args.get('report_id')
    if not report_id:
        return jsonify({"error": "Report ID is required"})

    if report_id:
        return jsonify({"status": "Complete", "report_data": report_id})
    else:
        return jsonify({"status": "Running"})

def automatic_report_generation():
    while True:
        report_id = str(uuid.uuid4())
        store_ids = [1, 2, 3]
        for store_id in store_ids:
            report = generate_store_report(store_id)
        time.sleep(3600)

if __name__ == '__main__':
    report_thread = threading.Thread(target=automatic_report_generation)
    report_thread.daemon = True
    report_thread.start()
    app.run(debug=True)
