1. The Students List

To 'api/students/' the api end point

    http://127.0.0.1:8000/api/students/

Input json
    Name:
    Roll Number
    Date of Birth:
    Marks Percentage:
    Class Group:
    Father's Name:

Output json
{
    "students": [
        {
            "id": 1,
            "name": "Sudhakar Reddy",
            "roll_no": 1,
            "dob": "2000-10-06",
            "marks_percentage": 85,
            "class_group": "A",
            "father_name": "Subbareddy"
        },
        {
            "id": 2,
            "name": "Ravindra Reddy",
            "roll_no": 2,
            "dob": "1991-12-12",
            "marks_percentage": 85,
            "class_group": "B",
            "father_name": "RamanaReddy"
        },
        {
            "id": 3,
            "name": "Pradeep",
            "roll_no": 3,
            "dob": "1999-10-07",
            "marks_percentage": 76,
            "class_group": "A",
            "father_name": "Venkatesh"
        },
        {
            "id": 4,
            "name": "Arjun",
            "roll_no": 4,
            "dob": "1997-10-06",
            "marks_percentage": 66,
            "class_group": "B",
            "father_name": "Aravind"
        },
        {
            "id": 5,
            "name": "Test",
            "roll_no": 5,
            "dob": "2000-10-06",
            "marks_percentage": 85,
            "class_group": "B",
            "father_name": "Tester"
        },
        {
            "id": 6,
            "name": "Bhavya",
            "roll_no": 6,
            "dob": "2013-08-18",
            "marks_percentage": 35,
            "class_group": "B",
            "father_name": "Sujatha Reddy"
        }
    ]
}


2. The Student Add

To 'api/student/add/' the api end point

    http://127.0.0.1:8000/api/student/add/


Input json
    Name:
    Roll Number
    Date of Birth:
    Marks Percentage:
    Class Group:
    Father's Name:


Output json

{
    "status": 200,
    "message": "successfully added"
}



3. The Student Details for Perticular id end point


    api/student/<int:pk>/


Sample Request

    http://127.0.0.1:8000/api/student/1/

OutPut json

    {
    "student": {
        "id": 1,
        "name": "Sudhakar Reddy",
        "roll_no": 1,
        "dob": "2000-10-06",
        "marks_percentage": 85,
        "class_group": "A",
        "father_name": "Subbareddy"
    }
}



4. The Student add_marks per Perticulat id

    /api/student/2/add-mark/

Sample Request

    http://127.0.0.1:8000/api/student/2/add-mark/


Output json

    {
    "status": 200,
    "message": "successfully added"
}


5. To Update Student mark api end point

    http://localhost:8000/api/student/mark/?id=5

Input json id = 5

    {
    "marks": 25,
    "subject": "Physcis",
    "marks_percentage": 25
}

Output json

    {
    "status": 200,
    "message": "successfully updated"
}





6. To results the overall percantage api end point

    http://127.0.0.1:8000/api/student/results/


Output json

{
    "pass_percentage": 66.66666666666666
}

