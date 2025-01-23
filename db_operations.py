
import mysql.connector
from config.db_config import get_db_connection

def get_water_depth(city_name):
    # Establish the connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to fetch water depth based on site name (city)
    query = """
    SELECT wls_wtr_level
    FROM water_levels wl
    JOIN wells w ON wl.site_id = w.site_id
    WHERE w.site_name = %s
    LIMIT 1;
    """
    
    try:
        # Execute the query
        cursor.execute(query, (city_name,))
        result = cursor.fetchone()  # Fetch the first result
        
        if result:
            # If a result is found, return the water depth
            if result[0]>6:
                print("Low Water Alert !!! Use Water Carefully!!")
            else:
                print("You Have Sufficient Water!!")
            return result[0]
        else:

            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

