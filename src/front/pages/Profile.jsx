// src/front/js/pages/Profile.js
import React, { useEffect, useState } from "react";

const Profile = () => {
  const [profile, setProfile] = useState(null);
  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchProfile = async () => {
      const res = await fetch("http://127.0.0.1:3001/api/profile", {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      if (res.ok) {
        const data = await res.json();
        setProfile(data.user);
      } else {
        setProfile(null);
      }
    };

    fetchProfile();
  }, [token]);

  if (!token) return <p>❌ You must be logged in to view this page.</p>;
  if (!profile) return <p>Loading profile...</p>;

  return (
    <div>
      <h2>Welcome, {profile.first_name}!</h2>
      <p><strong>Email:</strong> {profile.email}</p>
      <p><strong>Username:</strong> {profile.username}</p>
      <p><strong>Role:</strong> {profile.role}</p>
    </div>
  );
};

export default Profile;
