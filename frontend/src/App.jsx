import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout";
import Home from "./pages/Home";

import Dashboard from "./pages/Dashboard";
import AIQuery from "./pages/AIQuery";
import ProductSearch from "./pages/ProductSearch";
import ImageSearch from "./pages/ImageSearch";
import FinishedGoods from "./pages/FinishedGoods";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* Welcome / Home page */}
        <Route path="/" element={<Home />} />

        {/* Main WFX application */}
        <Route element={<Layout />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/ai-query" element={<AIQuery />} />
          <Route path="/product-search" element={<ProductSearch />} />
          <Route path="/image-search" element={<ImageSearch />} />
          <Route path="/finished-goods" element={<FinishedGoods />} />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;