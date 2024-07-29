import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
# Таблица "Дроны"
cursor.execute("""
CREATE TABLE IF NOT EXIT tbl_drone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    max_altitude INTEGER,
    max_speed INTEGER,
    max_flight_time INTEGER,
    serial_number TEXT UNIQUE NOT NULL,
    payload INTEGER,
    model TEXT NOT NULL,
    manufacture TEXT NOT NULL,
    purchase_date DATE,
    software_version TEXT,
    battery_capacity INTEGER,
    flight_hours INTEGER
)
""")

# Таблица "Статус"
cursor.execute("""
CREATE TABLE IF NOT EXIT tbl_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# Таблица "Статус Дронов"
cursor.execute("""
CREATE TABLE IF NOT EXIT tbl_drones_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    mission_id INTEGER NOT NULL,
    operator_id INTEGER NOT NULL,
    status_update_time DATETIME NOT NULL,
    battery_level INTEGER NOT NULL,
    coordinate TEXT,
    is_flying BOOLEAN,
    FOREIGN KEY (drone_id) REFERENCE tbl_drones(id)
    FOREIGN KEY (status_id) REFERENCE tbl_status(id)
    FOREIGN KEY (mission_id) REFERENCE tbl_mission(id)
    FOREIGN KEY (operator_id) REFERENCE tbl_operators(id)
)
""")

# Таблица "Техническое обслуживание"
cursor.execute("""
CREATE TABLE IF NOT EXIT tbl_maintenance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_id INTEGER NOT NULL,
    last_maintenance DATE,
    description TEXT,
    FOREIGN KEY (drone_id) REFERENCE tbl_drones(id)
)
""")

# Таблица "Миссия"