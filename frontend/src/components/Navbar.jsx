import { NavLink } from "react-router-dom";

function Navbar({ darkMode, setDarkMode }) {
  return (
    <aside className="sidebar">

      <div className="sidebar-brand">
        <div className="brand-logo">W</div>

        <div>
          <div className="brand-name">WFX</div>
          <div className="brand-subtitle">ERP Intelligence</div>
        </div>
      </div>

      <div className="sidebar-section-title">
        MAIN
      </div>

      <nav className="sidebar-nav">

        <NavLink
          to="/dashboard"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <span>▦</span>
          Dashboard
        </NavLink>

        <NavLink
          to="/ai-query"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <span>✦</span>
          AI Query
        </NavLink>

        <NavLink
          to="/product-search"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <span>⌕</span>
          Product Search
        </NavLink>

        <NavLink
          to="/image-search"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <span>▧</span>
          Image Search
        </NavLink>

        <NavLink
          to="/finished-goods"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <span>◫</span>
          Finished Goods
        </NavLink>

      </nav>

      <div className="sidebar-bottom">

        <button
          className="theme-toggle"
          onClick={() => setDarkMode(!darkMode)}
        >
          <span>
            {darkMode ? "☀" : "☾"}
          </span>

          {darkMode ? "Light Mode" : "Dark Mode"}
        </button>

        <div className="sidebar-footer">
          WFX ERP
          <span>v1.0</span>
        </div>

      </div>

    </aside>
  );
}

export default Navbar;