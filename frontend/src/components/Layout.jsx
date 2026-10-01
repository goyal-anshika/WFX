import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import { useState } from "react";

function Layout() {

  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={darkMode ? "app dark-mode" : "app"}>

      <Navbar
        darkMode={darkMode}
        setDarkMode={setDarkMode}
      />

      <div className="page-wrapper">

        <header className="topbar">

          <div className="topbar-title">
            WFX Intelligence Platform
          </div>

          <div className="topbar-status">
            <span className="status-dot"></span>
            System Online
          </div>

        </header>

        <main className="main-content">
          <Outlet />
        </main>

      </div>

    </div>
  );
}

export default Layout;