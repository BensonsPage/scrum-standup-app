# Use the official MySQL image as a base
FROM mysql:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Set the default user for the MySQL image

COPY init.sql /docker-entrypoint-initdb.d/
RUN ["chmod", "777", "/docker-entrypoint-initdb.d/init.sql"]

# scrum*ndup

ENV MYSQL_ROOT_PASSWORD = environ.get('MYSQL_ROOT_PASSWORD')

# Expose port 3306 to allow connections to the database
EXPOSE 3306

# Start the MySQL server when the container is run
CMD ["mysqld"]

# VOLUME /db_data