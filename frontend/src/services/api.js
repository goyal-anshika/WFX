import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const getDashboardStats = async () => {
  const response = await api.get("/api/dashboard/stats");
  return response.data;
};

export const askAI = async (question) => {
  const response = await api.post("/api/ai/query", {
    question,
  });

  return response.data;
};

export const searchProducts = async ({
  q = "*",
  page = 1,
  per_page = 20,
  category,
  fabric,
  color,
  print_type,
  season,
  brand,
  sort_by,
}) => {
  const response = await api.get("/api/search/products", {
    params: {
      q,
      page,
      per_page,
      category,
      fabric,
      color,
      print_type,
      season,
      brand,
      sort_by,
    },
  });

  return response.data;
};

export default api;