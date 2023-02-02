-- Cargos possíveis para um funcionário
CREATE TABLE Roles (
    RoleId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    RoleName NVARCHAR(20) NOT NULL
);

-- Dados de um funcionário (usuário do sistema)
CREATE TABLE Employees (
    EmployeeId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    Username NVARCHAR(30) NOT NULL,
    Password NVARCHAR(30) NOT NULL,
    CompleteName NVARCHAR(50) NOT NULL,
    RoleId INT NOT NULL,
    FOREIGN KEY (RoleId) REFERENCES Roles(RoleId),
    UNIQUE(Username)
);

-- Assuntos de atividades existentes
CREATE TABLE Subjects(
    SubjectId INT IDENTITY (1, 1) PRIMARY KEY NOT NULL,
    SubjectName NVARCHAR(20) NOT NULL
);

-- Assuntos sobre os quais um tutor pode criar uma nova atividade
CREATE TABLE TutorSubjects(
    TutorId INT NOT NULL,
    SubjectId INT NOT NULL,
    FOREIGN KEY (TutorId) REFERENCES Employees(EmployeeId),
    FOREIGN KEY (SubjectId) REFERENCES Subjects(SubjectId)
);

-- Atividades
CREATE TABLE Activities(
    ActivityId INT IDENTITY(1, 1) NOT NULL,
    TutorId INT NOT NULL, -- Tutor responsável pela atividade 
    SubjectId INT NOT NULL, -- Assunto da atividade
    MeetingPlace NVARCHAR(50) NOT NULL
    StartDate DATETIME NOT NULL, -- Data de ocorrência da atividade
    SlotsAmount INT NOT NULL, -- Número de participantes máximo (Mentoria = 1, Workshops > 1)
    Finished BIT NOT NULL, -- Atividade já foi terminada
    FOREIGN KEY (TutorId) REFERENCES Employees(EmployeeId),
    FOREIGN KEY (SubjectId) REFERENCES Subjects(SubjectId)
);

-- Alocação de atividades
CREATE TABLE ActivityAllocation(
    ActivityId INT NOT NULL,
    EmployeeId INT NOT NULL,
    FOREIGN KEY (ActivityId) REFERENCES Activities(ActivityId),
    FOREIGN KEY (EmployeeId) REFERENCES Employees(EmployeeId)
);

-- Avaliação de usuário por evento
CREATE TABLE ActivitiesRatings(
    ActivityId INT NOT NULL,
    EmployeeId INT NOT NULL,
    Rating DECIMAL (4, 2) NOT NULL, 
    WrittenFeedback NVARCHAR(250) NULL,
    FOREIGN KEY (ActivityId) REFERENCES Activities(ActivityId),
    FOREIGN KEY (EmployeeId) REFERENCES Employees(EmployeeId)
);

