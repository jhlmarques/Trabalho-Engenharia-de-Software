delete from Activities
delete from ActivitiesRatings
delete from ActivityAllocation
delete from Employees
delete from Roles
delete from Subjects
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
    ('CarusoVitor', 'cox1nh4123', 'Vitor Caruso Rodrigues Ferrer', 2),         
    ('Hernandes', 'xurr@ascoGostoso', 'Léo Hernandes de Vasconcelos', 1),      
    ('Jose', 'comelasmina', 'José Henrique Lima Marques', 1),                  
    ('burno', 'abacate', 'Bruno Grohs Vergara', 1),                            
    ('arumeida', 'empadinha', 'Matheus Almeida Silva', 2),                     
    ('round_robin', 'HerbertRichers666', 'Robert Rogers dos Santos Silva', 3); 

INSERT INTO TutorSubjects (TutorId, SubjectId)
VALUES
    (1, 6),
    (1, 5),
    (2, 7),
    (2, 1),
    (2, 3)

INSERT INTO Activities (TutorId, SubjectId, MeetingPlace, StartDate, SlotsAmount, Finished)
VALUES
    (1, 6, 'Auditório Robert Rogers', '20230318 16:40:00', 350, 0),
    (1, 5, 'Online', '20201111 16:40:00', 1, 1),
    (1, 7, 'Auditório Taz Mania', '20230422 13:40:00', 100, 0),
    (1, 2, 'Sala Zézinho', '20230422 13:40:00', 10, 0)