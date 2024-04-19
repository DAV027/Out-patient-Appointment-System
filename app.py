from flask import Flask, request, jsonify

from models import mongo, Appointment

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/appointment_system"
mongo.init_app(app)

# API endpoints

@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = mongo.db.doctors.find()
    return jsonify([{
        '_id': str(doctor['_id']),
        'name': doctor['name'],
        'specialty': doctor['specialty'],
        'schedule': doctor['schedule']
    } for doctor in doctors])

@app.route('/doctors/<doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = mongo.db.doctors.find_one_or_404({'_id': doctor_id})
    return jsonify({
        '_id': str(doctor['_id']),
        'name': doctor['name'],
        'specialty': doctor['specialty'],
        'schedule': doctor['schedule']
    })

@app.route('/doctors/<doctor_id>/availability', methods=['GET'])
def check_availability(doctor_id):
    return jsonify({})

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    doctor_id = data['doctor_id']
    date = data['date']
    patient_name = data['patient_name']

    appointment = Appointment(doctor_id, date, patient_name)
    mongo.db.appointments.insert_one(appointment.__dict__)

    return jsonify({'message': 'Appointment booked successfully'})

if __name__ == '__main__':
    app.run(debug=True)
