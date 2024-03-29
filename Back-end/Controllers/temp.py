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
    
    connection = mysql.connector.connect(host='localhost', database='mydb', user='root', password='*password*')
    cursor = connection.cursor(prepared=True)
    Insertquery = "INSERT INTO `meeting` (`MeetingID`, `Name`, `MeetingRooms`, `MeetingTopic`, `Date`, `StartTime`, `EndTime`, `Attendee`, `NeedHarware`, `Status`, `IsRoutine`, `Requires`, `Sites`, `Outline`, `Initiator`, `Memo`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    meetingid = package["id"]
    meetingname = generate_name(package["id"])
    meetingtopic = package["meeting_topic"]
    meetingrooms = package["meeting_rooms"]
    meetingdate = convert_date(int(package["start_timestamp"])/1000)
    meetingst = convert_time(int(package["start_timestamp"])/1000)
    meetinget = convert_time(int(package["end_timestamp"])/1000)
    meetinghw = package["need_hw_support"]
    meetingattendees = package["attendees"]
    meetingroutine = package["is_routine"]
    meetingrequires = package["need_hw_support"]
    meetingsites = package["sites"]
    meetingoutline = package["meeting_outline"]
    meetinginitiator = package["initiator"]
    meetingstatus = package["status"]
    meetingmemo = package["meeting_memo"]
    datatuple = (meetingid,meetingname,meetingrooms,meetingtopic,meetingdate,meetingst,meetinget,meetingattendees,meetinghw,meetingstatus,meetingroutine,meetingrequires,meetingsites,meetingoutline,meetinginitiator,meetingmemo)
    cursor.execute(Insertquery,datatuple)
    connection.commit()
    cursor.close()
    connection.close()



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

