<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scheduling System</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Faculty and Room Scheduling System</h1>
  <div class="form-container">
    <form id="scheduleForm">
      <label for="faculty">Faculty Name:</label>
      <input type="text" id="faculty" name="faculty" required>
      
      <label for="course">Course:</label>
      <input type="text" id="course" name="course" required>
      
      <label for="room">Room:</label>
      <input type="text" id="room" name="room" required>
      
      <label for="time">Preferred Time Slot:</label>
      <input type="time" id="time" name="time" required>
      
      <button type="submit">Submit</button>
    </form>
  </div>
  <div id="scheduleOutput"></div>
  <script src="app.js"></script>
</body>
</html>