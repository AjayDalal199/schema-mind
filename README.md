# SchemaMind

SchemaMind is a **backend-first OCR and schema-based structured extraction service**.  
It allows users to upload documents, extract text using OCR, and transform unstructured content into **validated, structured JSON** using user-defined schemas.

The project is designed as a **production-grade API service**, built with scalability, security, and asynchronous processing in mind.

---

## What SchemaMind Does

SchemaMind solves the problem of turning scanned or unstructured documents into **usable, typed data**.

With SchemaMind, users can:

- Upload documents (PDFs, images)
- Extract raw text using OCR
- View extracted content in multiple formats:
  - Plain text
  - Markdown
  - JSON
- Define custom schemas (field name, type, description)
- Run schema-based extraction to get structured, validated data
- Retrieve results via secure APIs

---

## Core Concepts

### OCR Extraction

Documents are processed asynchronously to extract raw text and metadata such as page count and confidence scores.

### Schema-Based Extraction

Instead of returning only raw text, SchemaMind allows users to define **schemas** describing what data they want.

Example schema fields:

- invoice_number (string)
- invoice_date (date)
- total_amount (number)

SchemaMind maps OCR text to these fields and returns structured output with confidence scores.

---

## Technology Stack

- **Language:** Python
- **API Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy / SQLModel
- **Authentication:** JWT
- **Async Processing:** Background workers (Celery / RQ / Taskiq)
- **Storage:** Local (development), S3-compatible storage (production)
- **Migrations:** Alembic

---

## Key Features

- JWT-based authentication and authorization
- Secure document upload and storage
- Asynchronous OCR processing
- Multi-format OCR output (text, markdown, JSON)
- User-defined schema templates
- Schema-based structured data extraction
- Field-level confidence scoring
- Production-ready architecture

---

## API-First Design

SchemaMind is designed as a **headless backend service**.

- No frontend assumptions
- RESTful APIs for all functionality
- Easy integration with web apps, mobile apps, or other services

---

## Project Status

🚧 **Under active development**

Current focus:

- Backend architecture
- Database schema
- OCR pipeline
- Schema-based extraction engine

---

## Roadmap (High-Level)

- [ ] Authentication & user management
- [ ] Document upload & lifecycle management
- [ ] Asynchronous OCR processing
- [ ] OCR result storage & retrieval
- [ ] Schema CRUD APIs
- [ ] Schema-based extraction engine
- [ ] Validation & confidence scoring
- [ ] Dockerized production deployment

---

## Non-Goals (Initial Version)

- Frontend UI
- Handwriting-specific OCR optimization
- Nested or conditional schemas
- Automatic schema generation
- Cross-document search

---

## Contributing

This project is currently in early development.  
Contribution guidelines will be added once the core architecture is stabilized.

---

## License

License information will be added later.

---

## Author

Built as a production-grade backend system to explore:

- OCR pipelines
- Asynchronous processing
- Schema-driven data extraction
- Scalable API design
