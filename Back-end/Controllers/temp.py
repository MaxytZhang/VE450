#!flask/bin/python

@app.route('/backend/api/v1.0/meeting_submit', methods=['GET','POST'])
def submit_meeting():
    package = request.form
    if not package["type"] == "meeting":
        return jsonify(make_package("error","error - sending wrong data"))
    meeting_info = package
    



@app.route('/backend/api/v1.0/meeting_submit', methods=['GET','POST'])