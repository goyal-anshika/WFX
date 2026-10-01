function ProductCard({ product }) {
  return (
    <div className="product-card">

      {product.image_url && (
        <img
          src={product.image_url}
          alt={product.style_name || product.style_number}
          className="product-image"
        />
      )}

      <div className="product-info">

        <h3>{product.style_name || "Unnamed Product"}</h3>

        <p className="style-number">
          {product.style_number}
        </p>

        <p>
          <strong>Category:</strong>{" "}
          {product.category || "—"}
        </p>

        <p>
          <strong>Fabric:</strong>{" "}
          {product.fabric || "—"}
        </p>

        <p>
          <strong>Color:</strong>{" "}
          {product.color || "—"}
        </p>

        <p>
          <strong>Brand:</strong>{" "}
          {product.brand || "—"}
        </p>

        {product.selling_price !== undefined && (
          <p>
            <strong>Price:</strong>{" "}
            ₹{product.selling_price}
          </p>
        )}

      </div>
    </div>
  );
}

export default ProductCard;