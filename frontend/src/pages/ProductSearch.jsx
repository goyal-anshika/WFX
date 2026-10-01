import { useEffect, useState } from "react";

import {
  searchProducts
} from "../services/api";

import ProductCard from "../components/ProductCard";
import Loading from "../components/Loading";


function ProductSearch() {

  const [query, setQuery] = useState("*");

  const [filters, setFilters] = useState({
    category: "",
    fabric: "",
    color: "",
    printType: "",
    season: "",
    brand: "",
  });

  const [products, setProducts] = useState([]);
  const [facets, setFacets] = useState({});

  const [page, setPage] = useState(1);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const loadProducts = async () => {

    setLoading(true);
    setError("");

    try {

      const data = await searchProducts({
        q: query || "*",
        page,
        perPage: 20,

        category: filters.category,
        fabric: filters.fabric,
        color: filters.color,
        printType: filters.printType,
        season: filters.season,
        brand: filters.brand,
      });

      setProducts(data.hits || []);
      setFacets(data.facet_counts || {});

    } catch (err) {

      setError(
        err.response?.data?.detail ||
        "Unable to search products."
      );

    } finally {

      setLoading(false);

    }
  };


  useEffect(() => {
    loadProducts();
  }, [page]);


  const handleSearch = (event) => {

    event.preventDefault();

    setPage(1);

    loadProducts();
  };


  const handleFilterChange = (event) => {

    const {
      name,
      value
    } = event.target;

    setFilters((previous) => ({
      ...previous,
      [name]: value,
    }));

  };


  return (
    <div className="page">

      <div className="page-header">
        <h1>Product Search</h1>
        <p>
          Search and filter finished goods.
        </p>
      </div>


      <form
        className="search-bar"
        onSubmit={handleSearch}
      >

        <input
          value={query === "*" ? "" : query}
          onChange={(e) =>
            setQuery(e.target.value)
          }
          placeholder="Search products..."
        />

        <button type="submit">
          Search
        </button>

      </form>


      <div className="filters">

        <input
          name="category"
          placeholder="Category"
          value={filters.category}
          onChange={handleFilterChange}
        />

        <input
          name="fabric"
          placeholder="Fabric"
          value={filters.fabric}
          onChange={handleFilterChange}
        />

        <input
          name="color"
          placeholder="Color"
          value={filters.color}
          onChange={handleFilterChange}
        />

        <input
          name="printType"
          placeholder="Print"
          value={filters.printType}
          onChange={handleFilterChange}
        />

        <input
          name="season"
          placeholder="Season"
          value={filters.season}
          onChange={handleFilterChange}
        />

        <input
          name="brand"
          placeholder="Brand"
          value={filters.brand}
          onChange={handleFilterChange}
        />

        <button
          type="button"
          onClick={() => {
            setPage(1);
            loadProducts();
          }}
        >
          Apply Filters
        </button>

      </div>


      {error && (
        <div className="error">
          {error}
        </div>
      )}


      {loading ? (

        <Loading text="Searching products..." />

      ) : (

        <>
          <div className="results-header">
            <span>
              {products.length} products shown
            </span>
          </div>


          <div className="product-grid">

            {products.map((item, index) => {

              const product =
                item.document || item;

              return (
                <ProductCard
                  key={
                    product.id ||
                    product.style_number ||
                    index
                  }
                  product={product}
                />
              );

            })}

          </div>


          {products.length === 0 && (
            <div className="empty">
              No products found.
            </div>
          )}


          <div className="pagination">

            <button
              disabled={page === 1}
              onClick={() =>
                setPage((p) => p - 1)
              }
            >
              Previous
            </button>

            <span>
              Page {page}
            </span>

            <button
              disabled={products.length < 20}
              onClick={() =>
                setPage((p) => p + 1)
              }
            >
              Next
            </button>

          </div>

        </>

      )}

    </div>
  );
}

export default ProductSearch;