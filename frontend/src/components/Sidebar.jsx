import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Package,
  Sparkles,
  Image,
  Search,
  Home,
} from "lucide-react";

const navigation = [
  {
    name: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Products",
    path: "/products",
    icon: Package,
  },
  {
    name: "Product Search",
    path: "/search",
    icon: Search,
  },
  {
    name: "AI Assistant",
    path: "/ai",
    icon: Sparkles,
  },
  {
    name: "Image Search",
    path: "/image-search",
    icon: Image,
  },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-logo">
        <div className="wfx-mark">W</div>

        <div>
          <div className="wfx-name">WFX</div>
          <div className="wfx-subtitle">
            Fashion Intelligence
          </div>
        </div>
      </div>

      <nav className="sidebar-nav">
        <NavLink
          to="/"
          className="sidebar-link"
        >
          <Home size={18} />
          Home
        </NavLink>

        {navigation.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `sidebar-link ${
                  isActive ? "active" : ""
                }`
              }
            >
              <Icon size={18} />
              {item.name}
            </NavLink>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <div className="sidebar-status">
          <span className="status-dot" />
          System Online
        </div>
      </div>
    </aside>
  );
}