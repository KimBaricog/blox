import { useState, useEffect } from "react";
import axios from "axios";

export default function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");

  // Get users from Flask when page loads
  useEffect(() => {
    axios.get("http://localhost:5000/users").then((res) => setUsers(res.data));
  }, []);

  // Send new user to Flask
  const addUser = () => {
    axios.post("http://localhost:5000/add_user", { name }).then(() => {
      setUsers([...users, { name }]);
      setName("");
    });
  };

  return (
    <div>
      <h1>Users</h1>

      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter name"
      />
      <button onClick={addUser}>Addd</button>

      <ul>
        {users.map((u, i) => (
          <li key={i}>{u.name}</li>
        ))}
      </ul>
    </div>
  );
}
