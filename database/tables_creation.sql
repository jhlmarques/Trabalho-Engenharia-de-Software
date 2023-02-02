CREATE TABLE Roles (
    RoleId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    RoleName NVARCHAR(20) NOT NULL
);

CREATE TABLE Employees (
    EmployeeId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    Username NVARCHAR(30) NOT NULL,
    Password NVARCHAR(30) NOT NULL,
    CompleteName NVARCHAR(50) NOT NULL,
    RoleId INT NOT NULL,
    FOREIGN KEY (RoleId) REFERENCES Roles(RoleId)
);

CREATE TABLE Subjects(
    SubjectId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    SubjectName NVARCHAR(20) NOT NULL
);

CREATE TABLE Mentorships(
    MentorshipId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    MentorId INT NOT NULL,
    SubjectId INT NOT NULL,
    FOREIGN KEY (MentorId) REFERENCES Employees(EmployeeId),
    FOREIGN KEY (SubjectId) REFERENCES Subjects(SubjectId)
);

CREATE TABLE MentorshipHistory(
    MentorshipId INT NOT NULL,
    MentoredId INT NOT NULL,
    StartDate DATETIME NOT NULL,
    MentorRating DECIMAL(2,2) NULL,
    MentoredRating DECIMAL(2,2) NULL,
    MentoredFeedback NVARCHAR(250) NULL,
    Canceled BIT NOT NULL,
    PRIMARY KEY(MentorshipId, StartDate),
    FOREIGN KEY (MentoredId) REFERENCES Employees(EmployeeId),
    FOREIGN KEY (MentorshipId) REFERENCES Mentorships(MentorshipId)
);

CREATE TABLE Workshops(
    WorkshopId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    MentorId INT NOT NULL,
    Title NVARCHAR(100) NOT NULL,
    SubjectId INT NOT NULL,
    StartDate DATETIME NOT NULL,
    MettingPlace NVARCHAR(50) NOT NULL,
    RemainingSeats int NOT NULL,
    Canceled BIT NOT NULL,
    FOREIGN KEY (MentorId) REFERENCES Employees(EmployeeId),
    FOREIGN KEY (SubjectId) REFERENCES Subjects(SubjectId)
);

CREATE TABLE WorkshopRatings(
    WorkshopId INT NOT NULL,
    EmployeeId UNIQUEIDENTIFIER,
    Rating DECIMAL(2,2) NULL,
    FOREIGN KEY (WorkshopId) REFERENCES Workshops(WorkshopId)
);