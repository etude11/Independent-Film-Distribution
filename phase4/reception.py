import pymysql
import os

def get_next_id(table, id_column):
    try:
        with con.cursor() as cursor:
            sql = f"SELECT MAX({id_column}) as max_id FROM {table}"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['max_id'] + 1 if result['max_id'] else 1
    except Exception as e:
        print(f"Error getting next ID for {table}:", e)
        return None

def insert_filmmaker():
    try:
        with con.cursor() as cursor:
            filmmaker_id = get_next_id('Filmmaker', 'FilmmakerID')
            name = input("Enter Name: ")
            biography = input("Enter Biography: ")
            phone_no = input("Enter Phone Number: ")
            email = input("Enter Email: ")

            sql = "INSERT INTO Filmmaker (FilmmakerID, Name, Biography, PhoneNo, Email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (filmmaker_id, name, biography, phone_no, email))
            con.commit()
            print("Filmmaker inserted successfully.")
    except Exception as e:
        print("Error inserting filmmaker:", e)

def insert_film():
    try:
        with con.cursor() as cursor:
            film_id = get_next_id('Film', 'FilmID')
            title = input("Enter Title: ")
            genre = input("Enter Genre: ")
            language = input("Enter Language: ")
            release_year = int(input("Enter Release Year: "))
            filmmaker_id = int(input("Enter Filmmaker ID: "))

            sql = "INSERT INTO Film (FilmID, Title, Genre, Language, ReleaseYear, FilmmakerID) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (film_id, title, genre, language, release_year, filmmaker_id))
            con.commit()
            print("Film inserted successfully.")
    except Exception as e:
        print("Error inserting film:", e)

def insert_advertisement():
    try:
        with con.cursor() as cursor:
            ad_id = get_next_id('Advertisement', 'AdID')
            advertiser_name = input("Enter Advertiser Name: ")
            ad_type = input("Enter Advertisement Type: ")

            sql = "INSERT INTO Advertisement (AdID, AdvertiserName, AdType) VALUES (%s, %s, %s)"
            cursor.execute(sql, (ad_id, advertiser_name, ad_type))
            con.commit()
            print("Advertisement inserted successfully.")
    except Exception as e:
        print("Error inserting advertisement:", e)

def insert_festival():
    try:
        with con.cursor() as cursor:
            festival_id = get_next_id('Festival', 'FestivalID')
            festival_name = input("Enter Festival Name: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")

            sql = "INSERT INTO Festival (FestivalID, FestivalName, StartDate, EndDate) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (festival_id, festival_name, start_date, end_date))
            con.commit()
            print("Festival inserted successfully.")
    except Exception as e:
        print("Error inserting festival:", e)

def insert_viewer():
    try:
        with con.cursor() as cursor:
            viewer_id = get_next_id('Viewer', 'ViewerID')
            num_watched_films = int(input("Enter Number of Watched Films: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            street = input("Enter Street: ")
            city = input("Enter City: ")
            country = input("Enter Country: ")
            postal_code = input("Enter Postal Code: ")

            sql = "INSERT INTO Viewer (ViewerID, NumWatchedFilms, Name, Email, Street, City, Country, PostalCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (viewer_id, num_watched_films, name, email, street, city, country, postal_code))
            con.commit()
            print("Viewer inserted successfully.")
    except Exception as e:
        print("Error inserting viewer:", e)

def insert_payment():
    try:
        with con.cursor() as cursor:
            payment_id = get_next_id('Payment', 'PaymentID')
            amount = float(input("Enter Amount: "))
            payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
            viewer_id = int(input("Enter Viewer ID: "))
            film_id = int(input("Enter Film ID: "))

            sql = "INSERT INTO Payment (PaymentID, Amount, PaymentDate, ViewerID, FilmID) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (payment_id, amount, payment_date, viewer_id, film_id))
            con.commit()
            print("Payment inserted successfully.")
    except Exception as e:
        print("Error inserting payment:", e)

def insert_review():
    try:
        with con.cursor() as cursor:
            review_id = get_next_id('Review', 'ReviewID')
            rating = int(input("Enter Rating (1-10): "))
            review_text = input("Enter Review Text: ")
            film_id = int(input("Enter Film ID: "))
            viewer_id = int(input("Enter Viewer ID: "))

            sql = "INSERT INTO Review (ReviewID, Rating, ReviewText, FilmID, ViewerID) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (review_id, rating, review_text, film_id, viewer_id))
            con.commit()
            print("Review inserted successfully.")
    except Exception as e:
        print("Error inserting review:", e)

def insert_ticket():
    try:
        with con.cursor() as cursor:
            ticket_id = get_next_id('Ticket', 'TicketID')
            viewer_id = int(input("Enter Viewer ID: "))
            festival_id = int(input("Enter Festival ID: "))
            access_type = input("Enter Access Type: ")

            sql = "INSERT INTO Ticket (TicketID, ViewerID, FestivalID, AccessType) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (ticket_id, viewer_id, festival_id, access_type))
            con.commit()
            print("Ticket inserted successfully.")
    except Exception as e:
        print("Error inserting ticket:", e)

def update_filmmaker():
    try:
        with con.cursor() as cursor:
            filmmaker_id = int(input("Enter Filmmaker ID to update: "))
            name = input("Enter new Name: ")
            biography = input("Enter new Biography: ")
            phone_no = input("Enter new Phone Number: ")
            email = input("Enter new Email: ")

            sql = "UPDATE Filmmaker SET Name=%s, Biography=%s, PhoneNo=%s, Email=%s WHERE FilmmakerID=%s"
            cursor.execute(sql, (name, biography, phone_no, email, filmmaker_id))
            con.commit()
            print("Filmmaker updated successfully.")
    except Exception as e:
        print("Error updating filmmaker:", e)

def update_film():
    try:
        with con.cursor() as cursor:
            film_id = int(input("Enter Film ID to update: "))
            title = input("Enter new Title: ")
            genre = input("Enter new Genre: ")
            language = input("Enter new Language: ")
            release_year = int(input("Enter new Release Year: "))
            filmmaker_id = int(input("Enter new Filmmaker ID: "))

            sql = "UPDATE Film SET Title=%s, Genre=%s, Language=%s, ReleaseYear=%s, FilmmakerID=%s WHERE FilmID=%s"
            cursor.execute(sql, (title, genre, language, release_year, filmmaker_id, film_id))
            con.commit()
            print("Film updated successfully.")
    except Exception as e:
        print("Error updating film:", e)

def update_advertisement():
    try:
        with con.cursor() as cursor:
            ad_id = int(input("Enter Advertisement ID to update: "))
            advertiser_name = input("Enter new Advertiser Name: ")
            ad_type = input("Enter new Advertisement Type: ")

            sql = "UPDATE Advertisement SET AdvertiserName=%s, AdType=%s WHERE AdID=%s"
            cursor.execute(sql, (advertiser_name, ad_type, ad_id))
            con.commit()
            print("Advertisement updated successfully.")
    except Exception as e:
        print("Error updating advertisement:", e)

def update_festival():
    try:
        with con.cursor() as cursor:
            festival_id = int(input("Enter Festival ID to update: "))
            festival_name = input("Enter new Festival Name: ")
            start_date = input("Enter new Start Date (YYYY-MM-DD): ")
            end_date = input("Enter new End Date (YYYY-MM-DD): ")

            sql = "UPDATE Festival SET FestivalName=%s, StartDate=%s, EndDate=%s WHERE FestivalID=%s"
            cursor.execute(sql, (festival_name, start_date, end_date, festival_id))
            con.commit()
            print("Festival updated successfully.")
    except Exception as e:
        print("Error updating festival:", e)

def update_viewer():
    try:
        with con.cursor() as cursor:
            viewer_id = int(input("Enter Viewer ID to update: "))
            num_watched_films = int(input("Enter new Number of Watched Films: "))
            name = input("Enter new Name: ")
            email = input("Enter new Email: ")
            street = input("Enter new Street: ")
            city = input("Enter new City: ")
            country = input("Enter new Country: ")
            postal_code = input("Enter new Postal Code: ")

            sql = "UPDATE Viewer SET NumWatchedFilms=%s, Name=%s, Email=%s, Street=%s, City=%s, Country=%s, PostalCode=%s WHERE ViewerID=%s"
            cursor.execute(sql, (num_watched_films, name, email, street, city, country, postal_code, viewer_id))
            con.commit()
            print("Viewer updated successfully.")
    except Exception as e:
        print("Error updating viewer:", e)

def delete_filmmaker():
    try:
        with con.cursor() as cursor:
            filmmaker_id = int(input("Enter Filmmaker ID to delete: "))

            sql = "DELETE FROM Filmmaker WHERE FilmmakerID=%s"
            cursor.execute(sql, (filmmaker_id,))
            con.commit()
            print("Filmmaker deleted successfully.")
    except Exception as e:
        print("Error deleting filmmaker:", e)

def delete_film():
    try:
        with con.cursor() as cursor:
            film_id = int(input("Enter Film ID to delete: "))

            sql = "DELETE FROM Film WHERE FilmID=%s"
            cursor.execute(sql, (film_id,))
            con.commit()
            print("Film deleted successfully.")
    except Exception as e:
        print("Error deleting film:", e)

def delete_advertisement():
    try:
        with con.cursor() as cursor:
            ad_id = int(input("Enter Advertisement ID to delete: "))

            sql = "DELETE FROM Advertisement WHERE AdID=%s"
            cursor.execute(sql, (ad_id,))
            con.commit()
            print("Advertisement deleted successfully.")
    except Exception as e:
        print("Error deleting advertisement:", e)

def delete_festival():
    try:
        with con.cursor() as cursor:
            festival_id = int(input("Enter Festival ID to delete: "))

            sql = "DELETE FROM Festival WHERE FestivalID=%s"
            cursor.execute(sql, (festival_id,))
            con.commit()
            print("Festival deleted successfully.")
    except Exception as e:
        print("Error deleting festival:", e)

def delete_viewer():
    try:
        with con.cursor() as cursor:
            viewer_id = int(input("Enter Viewer ID to delete: "))

            sql = "DELETE FROM Viewer WHERE ViewerID=%s"
            cursor.execute(sql, (viewer_id,))
            con.commit()
            print("Viewer deleted successfully.")
    except Exception as e:
        print("Error deleting viewer:", e)

def retrieve_films_by_filmmaker():
    try:
        with con.cursor() as cursor:
            filmmaker_id = int(input("Enter Filmmaker ID: "))

            sql = "SELECT * FROM Film WHERE FilmmakerID=%s"
            cursor.execute(sql, (filmmaker_id,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving films by filmmaker:", e)

def retrieve_films_by_viewer():
    try:
        with con.cursor() as cursor:
            viewer_id = int(input("Enter Viewer ID: "))

            sql = "SELECT * FROM Watches WHERE ViewedID=%s"
            cursor.execute(sql, (viewer_id,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving films by viewer:", e)

def retrieve_ads_by_film():
    try:
        with con.cursor() as cursor:
            film_id = int(input("Enter Film ID: "))

            sql = "SELECT * FROM Advertised WHERE FilmID=%s"
            cursor.execute(sql, (film_id,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving ads by film:", e)

def retrieve_viewers_by_film():
    try:
        with con.cursor() as cursor:
            film_id = int(input("Enter Film ID: "))

            sql = "SELECT Viewer.Name, Viewer.Email FROM Viewer JOIN Payment ON Viewer.ViewerID = Payment.ViewerID WHERE Payment.FilmID=%s"
            cursor.execute(sql, (film_id,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving viewers by film:", e)

def retrieve_films_by_festival():
    try:
        with con.cursor() as cursor:
            festival_id = int(input("Enter Festival ID: "))

            sql = "SELECT * FROM Submits WHERE FestivalID=%s"
            cursor.execute(sql, (festival_id,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving films by festival:", e)

def retrieve_viewers_by_festival():
    try:
        with con.cursor() as cursor:
            festival_id = int(input("Enter Festival ID: "))

            sql = "SELECT * FROM Ticket WHERE FestivalID=%s"
            cursor.execute(sql, (festival_id,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving viewers by festival:", e)

def retrieve_films_by_genre():
    try:
        with con.cursor() as cursor:
            genre = input("Enter Genre: ")

            sql = "SELECT * FROM Film WHERE Genre=%s"
            cursor.execute(sql, (genre,))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving films by genre:", e)

def calculate_total_revenue():
    try:
        with con.cursor() as cursor:
            sql = "SELECT SUM(Amount) as TotalRevenue FROM Payment"
            cursor.execute(sql)
            result = cursor.fetchone()
            print("Total Revenue:", result['TotalRevenue'])
    except Exception as e:
        print("Error calculating total revenue:", e)

def top_10_films_by_viewers():
    try:
        with con.cursor() as cursor:
            sql = "SELECT FilmID, COUNT(ViewedID) as NumViewers FROM Watches GROUP BY FilmID ORDER BY NumViewers DESC LIMIT 10"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving top 10 films by viewers:", e)

def top_10_grossing_films():
    try:
        with con.cursor() as cursor:
            sql = "SELECT FilmID, SUM(Amount) as TotalRevenue FROM Payment GROUP BY FilmID ORDER BY TotalRevenue DESC LIMIT 10"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving top 10 grossing films:", e)

def top_10_films_by_ratings():
    try:
        with con.cursor() as cursor:
            sql = "SELECT FilmID, AVG(Rating) as AvgRating FROM Review GROUP BY FilmID ORDER BY AvgRating DESC LIMIT 10"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving top 10 films by ratings:", e)

def total_revenue_by_filmmaker():
    try:
        with con.cursor() as cursor:
            filmmaker_id = int(input("Enter Filmmaker ID: "))

            sql = "SELECT SUM(Payment.Amount) as TotalRevenue FROM Payment JOIN Film ON Payment.FilmID = Film.FilmID WHERE Film.FilmmakerID=%s"
            cursor.execute(sql, (filmmaker_id,))
            result = cursor.fetchone()
            print("Total Revenue by Filmmaker:", result['TotalRevenue'])
    except Exception as e:
        print("Error calculating total revenue by filmmaker:", e)

def top_10_festivals_by_tickets():
    try:
        with con.cursor() as cursor:
            sql = "SELECT FestivalID, COUNT(TicketID) as NumTickets FROM Ticket GROUP BY FestivalID ORDER BY NumTickets DESC LIMIT 10"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        print("Error retrieving top 10 festivals by tickets:", e)

# Update the main_menu function to call the new functions
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """
    Main menu for operations.
    """
    print("\n--- Independent Film Platform ---")
    while True:
        print("Select operation\n")
        print("1. INSERT")
        print("2. UPDATE")
        print("3. DELETE")
        print("4. RETRIEVE")
        print("5. ANALYSIS")
        print("6. EXIT")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            execute_insert()
        elif choice == 2:
            execute_update()
        elif choice == 3:
            execute_delete()
        elif choice == 4:
            execute_retrieve()
        elif choice == 5:
            execute_analysis()
        elif choice == 6:
            print("Thank you for using the platform!")
            break
        else:
            print("Invalid choice. Please try again.")


def execute_insert():
    while True:
        print("\n--- Insert Menu ---")
        print("Select table to insert into\n")
        print("1. Register Filmmaker")
        print("2. Register Film")
        print("3. Register Advertisement")
        print("4. Register Festival")
        print("5. Register Viewer")
        print("6. Purchase Movie Ticket")
        print("7. Write Review")
        print("8. Buy Ticket")
        print("9. BACK TO MAIN MENU")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        clear_terminal()
        if choice == 1:
            insert_filmmaker()
        elif choice == 2:
            insert_film()
        elif choice == 3:
            insert_advertisement()
        elif choice == 4:
            insert_festival()
        elif choice == 5:
            insert_viewer()
        elif choice == 6:
            insert_payment()
        elif choice == 7:
            insert_review()
        elif choice == 8:
            insert_ticket()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

def execute_update():
    while True:
        print("\n--- Update Menu ---")
        print("Select table to update\n")
        print("1. Update Filmmaker")
        print("2. Update Film")
        print("3. Update Advertisement")
        print("4. Update Festival")
        print("5. Update Viewer")
        print("6. BACK TO MAIN MENU")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        clear_terminal()
        if choice == 1:
            update_filmmaker()
        elif choice == 2:
            update_film()
        elif choice == 3:
            update_advertisement()
        elif choice == 4:
            update_festival()
        elif choice == 5:
            update_viewer()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

def execute_delete():
    while True:
        print("\n--- Delete Menu ---")
        print("Select table to delete from\n")
        print("1. Delete Filmmaker")
        print("2. Delete Film")
        print("3. Delete Advertisement")
        print("4. Delete Festival")
        print("5. Delete Viewer")
        print("6. BACK TO MAIN MENU")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        clear_terminal()
        if choice == 1:
            delete_filmmaker()
        elif choice == 2:
            delete_film()
        elif choice == 3:
            delete_advertisement()
        elif choice == 4:
            delete_festival()
        elif choice == 5:
            delete_viewer()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

def execute_retrieve():
    while True:
        print("\n--- Retrieve Menu ---")
        print("1. Select all the films directed by a filmmaker")
        print("2. Select all the films watched by a viewer")
        print("3. Select all the advertisements featured in a film")
        print("4. Retrieve the names and email addresses of all viewers who have rented a specific film.")
        print("5. Select all the films featured in a festival")
        print("6. Select all the viewers who have bought a ticket for a festival")
        print("7. Select all the films with a specific genre")
        print("8. Calculate the total revenue generated from all film rentals.")
        print("9. BACK TO MAIN MENU")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        clear_terminal()
        if choice == 1:
            retrieve_films_by_filmmaker()
        elif choice == 2:
            retrieve_films_by_viewer()
        elif choice == 3:
            retrieve_ads_by_film()
        elif choice == 4:
            retrieve_viewers_by_film()
        elif choice == 5:
            retrieve_films_by_festival()
        elif choice == 6:
            retrieve_viewers_by_festival()
        elif choice == 7:
            retrieve_films_by_genre()
        elif choice == 8:
            calculate_total_revenue()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

def execute_analysis():
    while True:
        print("\n--- Analysis Menu ---")
        print("1. Top 10 films with the highest number of viewers")
        print("2. Top 10 grossing films")
        print("3. Top 10 films with the highest average ratings")
        print("4. Total revenue generated by a specific filmmaker")
        print("5. Top 10 festivals with the highest number of tickets sold")
        print("6. BACK TO MAIN MENU")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        clear_terminal()
        if choice == 1:
            top_10_films_by_viewers()
        elif choice == 2:
            top_10_grossing_films()
        elif choice == 3:
            top_10_films_by_ratings()
        elif choice == 4:
            total_revenue_by_filmmaker()
        elif choice == 5:
            top_10_festivals_by_tickets()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Establish connection to MySQL
    try:
        # Update database name as per your schema
        con = pymysql.connect(
            host='localhost',
            port=3306,
            user="root",
            password="admin123",
            db='IndependentFilmPlatform',
            cursorclass=pymysql.cursors.DictCursor
        )

        if con.open:
            print("Connected to the database!")
        else:
            print("Failed to connect to the database.")

        tmp = input("Press any key to continue...")
        
        try:
            main_menu()
        finally:
            con.close()
    except Exception as e:
        print("Error connecting to the database:", e)
