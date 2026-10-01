import { useEffect, useState } from "react";
import { Moon, Sun } from "lucide-react";

export default function ThemeToggle() {
  const [dark, setDark] = useState(() => {
    return localStorage.getItem("wfx-theme") === "dark";
  });

  useEffect(() => {
    document.documentElement.setAttribute(
      "data-theme",
      dark ? "dark" : "light"
    );

    localStorage.setItem(
      "wfx-theme",
      dark ? "dark" : "light"
    );
  }, [dark]);

  return (
    <button
      onClick={() => setDark(!dark)}
      className="theme-toggle"
      aria-label="Toggle theme"
    >
      {dark ? <Sun size={18} /> : <Moon size={18} />}
    </button>
  );
}