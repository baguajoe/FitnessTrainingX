import React from "react";
import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/signup">Signup</Link> |{" "}
        <Link to="/login">Login</Link> |{" "}
        <Link to="/profile">Profile</Link>
      </nav>
      <main>
        <Outlet />
      </main>
    </div>
  );
};

export default Layout; // ✅ REQUIRED
