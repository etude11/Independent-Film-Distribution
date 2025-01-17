CREATE DATABASE IF NOT EXISTS IndependentFilmPlatform;
USE IndependentFilmPlatform;

-- Drop tables if they exist
DROP TABLE IF EXISTS Refers;
DROP TABLE IF EXISTS Submits;
DROP TABLE IF EXISTS Follows;
DROP TABLE IF EXISTS Advertised;
DROP TABLE IF EXISTS Watches;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Viewer;
DROP TABLE IF EXISTS Festival;
DROP TABLE IF EXISTS Advertisement;
DROP TABLE IF EXISTS Film;
DROP TABLE IF EXISTS Filmmaker;

-- Filmmaker Table
CREATE TABLE Filmmaker (
    FilmmakerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Biography VARCHAR(4096),
    PhoneNo CHAR(10),
    Email VARCHAR(200)
);

-- Film Table
CREATE TABLE Film (
    FilmID INT PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(50),
    Language VARCHAR(50),
    ReleaseYear INT,
    FilmmakerID INT,
    FOREIGN KEY (FilmmakerID) REFERENCES Filmmaker(FilmmakerID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Advertisement Table
CREATE TABLE Advertisement (
    AdID INT PRIMARY KEY,
    AdvertiserName VARCHAR(50),
    AdType VARCHAR(30)
);

-- Festival Table
CREATE TABLE Festival (
    FestivalID INT PRIMARY KEY,
    FestivalName VARCHAR(100),
    StartDate DATE, 
    EndDate DATE
);

-- Viewer Table
CREATE TABLE Viewer (
    ViewerID INT PRIMARY KEY,
    NumWatchedFilms INT,
    Name VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Street VARCHAR(200),
    City VARCHAR(50),
    Country VARCHAR(50),
    PostalCode CHAR(6)
);

-- Payment Table
CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    Amount FLOAT CHECK (Amount > 0),
    PaymentDate DATE,
    ViewerID INT,
    FilmID INT,
    FOREIGN KEY (ViewerID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FilmID) REFERENCES Film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Review Table
CREATE TABLE Review (
    ReviewID INT PRIMARY KEY,
    Rating INT CHECK (Rating BETWEEN 1 AND 10),
    ReviewText VARCHAR(4096),
    FilmID INT,
    ViewerID INT,
    FOREIGN KEY (FilmID) REFERENCES Film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ViewerID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Ticket Table
CREATE TABLE Ticket (
    TicketID INT PRIMARY KEY,
    ViewerID INT,
    FestivalID INT,
    AccessType VARCHAR(30),
    FOREIGN KEY (ViewerID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FestivalID) REFERENCES Festival(FestivalID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Watches Table
CREATE TABLE Watches (
    ViewedID INT,
    FilmID INT,
    PRIMARY KEY (ViewedID, FilmID),
    FOREIGN KEY (ViewedID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FilmID) REFERENCES Film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Advertised Table
CREATE TABLE Advertised (
    AdID INT,
    FilmID INT,
    PRIMARY KEY (AdID, FilmID),
    FOREIGN KEY (AdID) REFERENCES Advertisement(AdID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FilmID) REFERENCES Film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Follows Table
CREATE TABLE Follows (
    FollowerID INT,
    FollowedID INT,
    PRIMARY KEY (FollowerID, FollowedID),
    FOREIGN KEY (FollowerID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FollowedID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Submits Table
CREATE TABLE Submits (
    SubmitID INT PRIMARY KEY,
    FilmID INT,
    FestivalID INT,
    FilmmakerID INT,
    FOREIGN KEY (FilmID) REFERENCES Film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FestivalID) REFERENCES Festival(FestivalID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FilmmakerID) REFERENCES Filmmaker(FilmmakerID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Refers Table
CREATE TABLE Refers (
    ReferrerID INT,
    ReferredID INT,
    PRIMARY KEY (ReferrerID, ReferredID),
    FOREIGN KEY (ReferrerID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ReferredID) REFERENCES Viewer(ViewerID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert data into tables
LOCK TABLES Filmmaker WRITE, Film WRITE, Advertisement WRITE, Festival WRITE, Viewer WRITE, Payment WRITE, Review WRITE, Ticket WRITE, Watches WRITE, Advertised WRITE, Follows WRITE, Submits WRITE, Refers WRITE;

INSERT INTO Filmmaker VALUES 
(1, 'John Doe', 'Biography of John Doe', '1234567890', 'john@example.com'),
(2, 'Jane Smith', 'Biography of Jane Smith', '0987654321', 'jane@example.com'),
(3, 'Alice Johnson', 'Biography of Alice Johnson', '1122334455', 'alice@example.com'),
(4, 'Bob Brown', 'Biography of Bob Brown', '2233445566', 'bob@example.com'),
(5, 'Charlie Davis', 'Biography of Charlie Davis', '3344556677', 'charlie@example.com'),
(6, 'Diana Evans', 'Biography of Diana Evans', '4455667788', 'diana@example.com'),
(7, 'Eve Foster', 'Biography of Eve Foster', '5566778899', 'eve@example.com'),
(8, 'Frank Green', 'Biography of Frank Green', '6677889900', 'frank@example.com'),
(9, 'Grace Harris', 'Biography of Grace Harris', '7788990011', 'grace@example.com'),
(10, 'Hank Irving', 'Biography of Hank Irving', '8899001122', 'hank@example.com');

INSERT INTO Film VALUES 
(1, 'Film Title 1', 'Drama', 'English', 2023, 1),
(2, 'Film Title 2', 'Comedy', 'French', 2022, 2),
(3, 'Film Title 3', 'Thriller', 'Spanish', 2021, 3),
(4, 'Film Title 4', 'Horror', 'German', 2020, 4),
(5, 'Film Title 5', 'Romance', 'Italian', 2019, 5),
(6, 'Film Title 6', 'Action', 'Japanese', 2018, 6),
(7, 'Film Title 7', 'Sci-Fi', 'Korean', 2017, 7),
(8, 'Film Title 8', 'Fantasy', 'Chinese', 2016, 8),
(9, 'Film Title 9', 'Documentary', 'Russian', 2015, 9),
(10, 'Film Title 10', 'Animation', 'Hindi', 2014, 10);

INSERT INTO Advertisement VALUES 
(1, 'Acme Corp', 'Banner'),
(2, 'Globex Corporation', 'Video'),
(3, 'Soylent Corp', 'Popup'),
(4, 'Initech', 'Banner'),
(5, 'Umbrella Corporation', 'Video'),
(6, 'Hooli', 'Popup'),
(7, 'Stark Industries', 'Banner'),
(8, 'Wayne Enterprises', 'Video'),
(9, 'Wonka Industries', 'Popup'),
(10, 'Cyberdyne Systems', 'Banner');

INSERT INTO Festival VALUES 
(1, 'Sundance Film Festival', '2023-01-01', '2023-01-10'),
(2, 'Cannes Film Festival', '2023-02-01', '2023-02-10'),
(3, 'Berlin International Film Festival', '2023-03-01', '2023-03-10'),
(4, 'Toronto International Film Festival', '2023-04-01', '2023-04-10'),
(5, 'Venice Film Festival', '2023-05-01', '2023-05-10'),
(6, 'SXSW Film Festival', '2023-06-01', '2023-06-10'),
(7, 'Tribeca Film Festival', '2023-07-01', '2023-07-10'),
(8, 'Edinburgh International Film Festival', '2023-08-01', '2023-08-10'),
(9, 'Locarno Film Festival', '2023-09-01', '2023-09-10'),
(10, 'San Sebastian Film Festival', '2023-10-01', '2023-10-10');

INSERT INTO Viewer VALUES 
(1, 10, 'Michael Johnson', 'michael.johnson@example.com', '123 Main St', 'New York', 'USA', '10001'),
(2, 20, 'Sarah Williams', 'sarah.williams@example.com', '456 Elm St', 'Los Angeles', 'USA', '90001'),
(3, 30, 'David Brown', 'david.brown@example.com', '789 Oak St', 'Chicago', 'USA', '60601'),
(4, 40, 'Emily Davis', 'emily.davis@example.com', '101 Pine St', 'Houston', 'USA', '77001'),
(5, 50, 'James Wilson', 'james.wilson@example.com', '202 Maple St', 'Phoenix', 'USA', '85001'),
(6, 60, 'Jessica Martinez', 'jessica.martinez@example.com', '303 Cedar St', 'Philadelphia', 'USA', '19101'),
(7, 70, 'John Anderson', 'john.anderson@example.com', '404 Birch St', 'San Antonio', 'USA', '78201'),
(8, 80, 'Laura Thomas', 'laura.thomas@example.com', '505 Walnut St', 'San Diego', 'USA', '92101'),
(9, 90, 'Robert Taylor', 'robert.taylor@example.com', '606 Ash St', 'Dallas', 'USA', '75201'),
(10, 100, 'Linda Moore', 'linda.moore@example.com', '707 Poplar St', 'San Jose', 'USA', '95101');

INSERT INTO Payment VALUES 
(1, 100.0, '2023-01-01', 1, 1),
(2, 200.0, '2023-02-01', 2, 2),
(3, 300.0, '2023-03-01', 3, 3),
(4, 400.0, '2023-04-01', 4, 4),
(5, 500.0, '2023-05-01', 5, 5),
(6, 600.0, '2023-06-01', 6, 6),
(7, 700.0, '2023-07-01', 7, 7),
(8, 800.0, '2023-08-01', 8, 8),
(9, 900.0, '2023-09-01', 9, 9),
(10, 1000.0, '2023-10-01', 10, 10);

INSERT INTO Review VALUES 
(1, 8, 'Great film!', 1, 1),
(2, 7, 'Good film!', 2, 2),
(3, 6, 'Decent film!', 3, 3),
(4, 5, 'Average film!', 4, 4),
(5, 4, 'Below average film!', 5, 5),
(6, 3, 'Not good!', 6, 6),
(7, 2, 'Bad film!', 7, 7),
(8, 1, 'Terrible film!', 8, 8),
(9, 9, 'Excellent film!', 9, 9),
(10, 10, 'Masterpiece!', 10, 10);

INSERT INTO Ticket VALUES 
(1, 1, 1, 'VIP'),
(2, 2, 2, 'Regular'),
(3, 3, 3, 'VIP'),
(4, 4, 4, 'Regular'),
(5, 5, 5, 'VIP'),
(6, 6, 6, 'Regular'),
(7, 7, 7, 'VIP'),
(8, 8, 8, 'Regular'),
(9, 9, 9, 'VIP'),
(10, 10, 10, 'Regular');

INSERT INTO Watches VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO Advertised VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO Follows VALUES 
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 1);

INSERT INTO Submits VALUES 
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5),
(6, 6, 6, 6),
(7, 7, 7, 7),
(8, 8, 8, 8),
(9, 9, 9, 9),
(10, 10, 10, 10);

INSERT INTO Refers VALUES 
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 1);

UNLOCK TABLES;