delete from Activities
DBCC Checkident (Activities, RESEED, 0);
delete from ActivitiesRatings
delete from ActivityAllocation
delete from Employees
DBCC Checkident (Employees, RESEED, 0);
delete from Roles
DBCC Checkident (Roles, RESEED, 0);
delete from Subjects
DBCC Checkident (Subjects, RESEED, 0);
delete from TutorSubjects

INSERT INTO Subjects (SubjectName)
VALUES
    ('Programação paralela'),
    ('Testes unitários'),    
    ('Autenticação JWT'),    
    ('Front-end em React'),  
    ('Back-end em Rust'),    
    ('Autoconhecimento'),    
    ('Prospecção');          

INSERT INTO Roles (RoleName)
VALUES
    ('Employee'),
    ('Mentor'),
    ('Manager');

INSERT INTO Employees (Username, Password, CompleteName, RoleId)
VALUES 
    ('CarusoVitor', 'cox1nh4123', 'Vitor Caruso Rodrigues Ferrer', 2),          -- 1 
    ('Hernandes', 'xurr@ascoGostoso', 'Léo Hernandes de Vasconcelos', 1),       -- 2  
    ('Jose', 'comelasmina', 'José Henrique Lima Marques', 1),                   -- 3 
    ('burno', 'abacate', 'Bruno Grohs Vergara', 1),                             -- 4  
    ('arumeida', 'empadinha', 'Matheus Almeida Silva', 2),                      -- 5 
    ('round_robin', 'HerbertRichers666', 'Robert Rogers dos Santos Silva', 3);  -- 6

INSERT INTO TutorSubjects (TutorId, SubjectId)
VALUES
    (1, 6),
    (1, 5),
    (5, 7),
    (5, 1),
    (5, 3);

INSERT INTO Activities (TutorId, SubjectId, MeetingPlace, StartDate, SlotsAmount, Finished)
VALUES
    (1, 6, 'Auditório Robert Rogers', '20230318 16:40:00', 350, 0), -- 1
    (1, 5, 'Online', '20201111 16:40:00', 1, 1),                    -- 2
    (5, 7, 'Auditório Taz Mania', '20230422 13:40:00', 100, 0),     -- 3
    (5, 2, 'Sala Zézinho', '20230422 13:40:00', 10, 0);             -- 4

INSERT INTO ActivityAllocation (ActivityId, EmployeeId)
VALUES
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 5),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 6),
    (4, 2),
    (4, 3),
    (4, 4);

INSERT INTO ActivitiesRatings(ActivityId, EmployeeId, Rating, WrittenFeedback)
VALUES
    (1, 5, 7.5, 'Bem esclarecedor, sinto que aprendi bastante de Rust agora mesmo sem ter entendido nada!'),
    (2, 2, 9.92, 'Gostei bastante, mas acho que pecou um pouco em não explicitar o return no slide 49.'),
    (3, 6, 8, 'Fiquei muito orgulhoso, vi esse muleque crescer. O problema é que eu não conseguia escutar nada lá de trás.'),
    (4, 4, 10, 'Incrível, fiquei sem palavras'),
    (4, 1, 0, NULL);

    