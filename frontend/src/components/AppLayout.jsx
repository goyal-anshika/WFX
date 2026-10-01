import { Outlet } from "react-router-dom";

import Sidebar from "./Sidebar";
import ThemeToggle from "./ThemeToggle";

import "../styles/layout.css";

export default function AppLayout() {
  return (
    <div className="app-layout">
      <Sidebar />

      <main className="main-content">
        <header className="topbar">
          <ThemeToggle />
        </header>

        <div className="page-container">
          <Outlet />
        </div>
      </main>
    </div>
  );
}