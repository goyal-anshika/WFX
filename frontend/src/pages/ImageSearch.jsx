import { useState } from "react";

import api from "../services/api";
import ProductCard from "../components/ProductCard";
import Loading from "../components/Loading";


function ImageSearch() {

  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handleSearch = async () => {

    if (!file) {
      setError("Please select an image first.");
      return;
    }

    setLoading(true);
    setError("");
    setResults([]);


    try {

      const formData = new FormData();

      formData.append(
        "file",
        file
      );


      const response = await api.post(
        "/api/image-search",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );


      setResults(
        response.data.results || []
      );

    } catch (err) {

      setError(
        err.response?.data?.detail ||
        "Image search failed."
      );

    } finally {

      setLoading(false);

    }

  };


  return (
    <div className="page">

      <div className="page-header">

        <h1>Image Search</h1>

        <p>
          Upload a garment image to find visually
          similar products.
        </p>

      </div>


      <div className="upload-box">

        <input
          type="file"
          accept="image/*"
          onChange={(e) =>
            setFile(e.target.files?.[0] || null)
          }
        />

        {file && (
          <p>
            Selected: {file.name}
          </p>
        )}


        <button
          onClick={handleSearch}
          disabled={!file || loading}
        >
          {loading
            ? "Searching..."
            : "Find Similar Products"}
        </button>

      </div>


      {error && (
        <div className="error">
          {error}
        </div>
      )}


      {loading && (
        <Loading
          text="Finding visually similar products..."
        />
      )}


      {!loading && results.length > 0 && (

        <>

          <h2>
            Similar Products
          </h2>

          <div className="product-grid">

            {results.map(
              (product, index) => (

                <div
                  key={
                    product.id ||
                    product.style_number ||
                    index
                  }
                >

                  <ProductCard
                    product={product}
                  />

                  <div className="similarity">
                    Similarity:{" "}
                    {(
                      Number(product.similarity) * 100
                    ).toFixed(1)}
                    %
                  </div>

                </div>

              )
            )}

          </div>

        </>

      )}


      {!loading &&
        file &&
        results.length === 0 &&
        !error && (

          <div className="empty">
            No similar products found.
          </div>

        )}

    </div>
  );
}

export default ImageSearch;