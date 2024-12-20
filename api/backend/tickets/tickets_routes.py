from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

tickets = Blueprint('tickets', __name__)

# ------------------------------------------------------------
# Route to view all tickets or filter by status/priority
@tickets.route('/tickets', methods=['GET'])
# Get all the products from the database, package them up,
# and return them to the client
def get_tickets():
    query = '''
        SELECT 
            *
        FROM Ticket
    '''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response


#------------------------------------------------------------
# Update customer info for customer with particular TicketID, Description, Status, Priority, TicketType, EmployeeID, StudentNUID
#   Notice the manner of constructing the query.
@tickets.route('/edit', methods=['PUT'])
def update_tickets():
    the_data = request.json
    current_app.logger.info(the_data)
   
    status = the_data['Status']
    priority = the_data['Priority']
    employeeID = the_data['EmployeeID']
    ticketID = the_data['TicketID']

    query = 'UPDATE Ticket SET Status = %s, Priority = %s, employeeID = %s Where TicketID = %s' 

    current_app.logger.info(query) 
    data = (status, priority, employeeID, ticketID)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response("Successfully edited ticket")
    response.status_code = 200
    
    return response


@tickets.route('/delete', methods=['DELETE'])
def delete_tickets():
    query = "DELETE FROM Ticket WHERE Status = %s"  
    

        # Execute the query with the parameter
    cursor = db.get_db().cursor()
    cursor.execute(query, ("Closed",))  # Tuple is used even for a single parameter
    
    db.get_db().commit()
    response = make_response("Successfully deleted closed tickets")
    response.status_code = 200
    return response


@tickets.route('/deletebyid', methods=['DELETE'])
def delete_specific_tickets():
    the_data = request.json
    current_app.logger.info(the_data)
    ticketID = the_data['TicketID']

    

    query = "DELETE FROM Ticket WHERE TicketID = %s"  
    
    current_app.logger.info(query)
    data = (ticketID)
    


        # Execute the query with the parameter
    cursor = db.get_db().cursor()
    cursor.execute(query, data)  # Tuple is used even for a single parameter
    
    db.get_db().commit()
    response = make_response("Successfully deleted specific ticket")
    response.status_code = 200
    return response

@tickets.route('/add', methods=['PUT'])
def add_ticket():
    """
    Adds a new ticket to the Ticket table in the database.
    """
    try:
        # Parse JSON request
        ticket_data = request.get_json()

        # Extract required fields
        description = ticket_data.get("Description")
        status = ticket_data.get("Status")
        priority = ticket_data.get("Priority")
        ticket_type = ticket_data.get("TicketType")
        employee_id = ticket_data.get("EmployeeID")
        student_nuid = ticket_data.get("StudentNUID")

        # Validate required fields
        if not all([description, status, priority, ticket_type, employee_id, student_nuid]):
            return jsonify({"error": "All fields are required."}), 400

        # SQL query to insert a new ticket
        query = '''
            INSERT INTO Ticket (Description, Status, Priority, TicketType, EmployeeID, StudentNUID)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (description, status, priority, ticket_type, employee_id, student_nuid)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()

        return jsonify({"message": "Ticket added successfully."}), 201

    except Exception as e:
        current_app.logger.error(f"Error adding ticket: {e}")
        return jsonify({"error": "Failed to add ticket."}), 500