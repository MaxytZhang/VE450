#!flask/bin/python

#open dB



@app.route('/backend/api/v1.0/meeting_submit', methods=['GET','POST'])
def submit_meeting():
    package = request.form
    if not package["type"] == "meeting":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    meeting_info = package



@app.route('/backend/api/v1.0/log_in', methods=['GET','POST'])
def employee_login():
    package = request.form
    if not package["type"] == "login":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    #check if the id and password match

    #if no, then return does not match

    #if yes, then return publish dashboard

@app.route('/backend/api/v1.0/more_notice', methods=['GET','POST'])
def load_more_notices():
    package = request.form
    if not package["type"] == "notices":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    #find all future meetings of the current user, meeting_id -> attendee_id -> feedback



@app.route('/backend/api/v1.0/meeting_history', methods=['GET','POST'])
def request_history():
    package = request.form
    if not package["type"] == "history":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    #find all meeting histories of the current user

@app.route('/backend/api/v1.0/check_meeting', methods=['GET','POST'])
def check_meeting():
    package = request.form
    if not package["type"] == "check":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    meeting_id = package["meeting_id"]
    #pull from the database

