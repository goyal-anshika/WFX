import { useEffect, useState } from "react";

import {
  searchProducts
} from "../services/api";

import ProductCard from "../components/ProductCard";
import Loading from "../components/Loading";


function FinishedGoods() {

  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(1);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");


  const loadProducts = async () => {

    setLoading(true);

    try {

      const data = await searchProducts({
        q: "*",
        page,
        perPage: 24,
      });

      setProducts(data.hits || []);

    } catch (err) {

      setError(
        err.response?.data?.detail ||
        "Unable to load finished goods."
      );

    } finally {

      setLoading(false);

    }
  };


  useEffect(() => {
    loadProducts();
  }, [page]);


  return (
    <div className="page">

      <div className="page-header">
        <h1>Finished Goods Explorer</h1>
        <p>
          Browse the WFX finished goods catalogue.
        </p>
      </div>


      {error && (
        <div className="error">
          {error}
        </div>
      )}


      {loading ? (

        <Loading text="Loading finished goods..." />

      ) : (

        <>

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
              disabled={products.length < 24}
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

export default FinishedGoods;