# React + FastAPI Application Requirements

## Goal: Family Information Data Analysis
The requirements for a React + FastAPI application that meets the above goal are described below.

Following the principles of object-oriented design, the requirements include the following:

## 1. Purpose
The overall purpose of the system is to provide an application that allows users to analyze family information data.

## 2. File and Folder Structure
### Frontend (React)
```
my-app/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Sidebar.js
│   │   ├── FamilyList.js
│   │   ├── FamilyDetails.js
│   │   └── ...
│   ├── pages/
│   │   ├── Dashboard.js
│   │   ├── Family.js
│   │   ├── Report.js
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   ├── helpers.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   ├── components.css
│   │   └── ...
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### Backend (FastAPI)
```
family_api/
├── app/
│   ├── models/
│   │   ├── family.py
│   │   ├── member.py
│   │   └── ...
│   ├── schemas/
│   │   ├── family.py
│   │   ├── member.py
│   │   └── ...
│   ├── routers/
│   │   ├── family.py
│   │   ├── member.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── test_family.py
│   ├── test_member.py
│   └── ...
├── requirements.txt
└── README.md
```

## 3. API Endpoints
The following API endpoints will be implemented using FastAPI:

| HTTP Method | Path | Description |
| --- | --- | --- |
| GET | /families | Retrieve a list of all families |
| GET | /families/{family_id} | Retrieve details of a specific family |
| POST | /families | Create a new family |
| PUT | /families/{family_id} | Update an existing family |
| DELETE | /families/{family_id} | Delete a family |
| GET | /members | Retrieve a list of all family members |
| GET | /members/{member_id} | Retrieve details of a specific family member |
| POST | /members | Create a new family member |
| PUT | /members/{member_id} | Update an existing family member |
| DELETE | /members/{member_id} | Delete a family member |

## 4. Data Models
The following data models will be defined using SQLAlchemy:

### Family
- id: int
- name: str
- address: str
- phone: str
- email: str
- members: List[Member]

### Member
- id: int
- first_name: str
- last_name: str
- age: int
- relationship: str
- family_id: int
- family: Family

## 5. React Components
The main React components for the application are:

- `Header`: Displays the application header and navigation menu.
- `Sidebar`: Provides a sidebar for navigation and filtering options.
- `FamilyList`: Displays a list of families with basic information.
- `FamilyDetails`: Shows detailed information about a specific family.
- `Dashboard`: The main landing page with overview and analytics.
- `Family`: Allows creating, updating, and deleting family information.
- `Report`: Generates reports and visualizations based on family data.

Each component will have its own set of props and state variables to manage the data and user interactions.

## 6. User Interface
### Screen Flow Diagram
![Screen Flow Diagram](screen_flow_diagram.png)

### Wireframes
The wireframes for the main screens of the application are available in the `wireframes/` folder.