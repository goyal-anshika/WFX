import { useEffect, useState } from "react";
import api from "../services/api";
import Loading from "../components/Loading";

function Dashboard() {
  const [stats, setStats] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const response = await api.get("/api/dashboard/stats");
      setStats(response.data);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Unable to load dashboard statistics."
      );
    }
  };

  if (error) {
    return (
      <div className="page">
        <h1>Dashboard</h1>
        <div className="error">{error}</div>
      </div>
    );
  }

  if (!stats) {
    return <Loading text="Loading dashboard..." />;
  }

  return (
    <div className="page">

      <div className="page-header">
        <h1>Dashboard</h1>
        <p>WFX ERP Overview</p>
      </div>

      <div className="stats-grid">

        <div className="stat-card">
          <span>Finished Goods</span>
          <strong>{stats.finished_goods}</strong>
        </div>

        <div className="stat-card">
          <span>Suppliers</span>
          <strong>{stats.suppliers}</strong>
        </div>

        <div className="stat-card">
          <span>Buyers</span>
          <strong>{stats.buyers}</strong>
        </div>

        <div className="stat-card">
          <span>Sales Orders</span>
          <strong>{stats.sales_orders}</strong>
        </div>

        <div className="stat-card">
          <span>Sales Invoices</span>
          <strong>{stats.sales_invoices}</strong>
        </div>

      </div>

    </div>
  );
}

export default Dashboard;