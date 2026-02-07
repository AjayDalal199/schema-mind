# SchemaMind – Backend Requirements Specification

## 1. Overview

SchemaMind is a backend-only, production-grade OCR and schema-based structured extraction service.
It allows authenticated users to upload documents, extract text using OCR, and transform unstructured text into validated, structured data using user-defined schemas.

The backend is designed to be secure, asynchronous, scalable, and suitable for real-world production deployment.

---

## 2. Technology Stack

- Programming Language: Python
- API Framework: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy / SQLModel
- Authentication: JWT (JSON Web Tokens)
- Background Processing: Asynchronous workers (Celery / RQ / Taskiq)
- File Storage: Local filesystem (development), S3-compatible object storage (production)
- Database Migrations: Alembic

---

## 3. Functional Requirements

### 3.1 Authentication & Authorization

- Users must be able to register and log in.
- Authentication must be implemented using JWT tokens.
- Passwords must be securely hashed.
- All non-auth endpoints must require authentication.
- Users must only be able to access their own data.

---

### 3.2 Document Upload & Management

- Users must be able to upload documents for OCR processing.
- Supported formats:
  - PDF
  - PNG
  - JPG
  - JPEG
- File size limits must be enforced.
- Uploaded files must be validated by MIME type.
- Each document must have a lifecycle status:
  - uploaded
  - processing
  - completed
  - failed
- Users must be able to list, retrieve, and delete their documents.
- Documents must be stored securely and must not be publicly accessible.

---

### 3.3 OCR Processing

- OCR must extract text from uploaded documents.
- OCR processing must be asynchronous.
- OCR jobs must not block API requests.
- OCR results must be stored persistently.
- OCR metadata must include:
  - language (if available)
  - page count
  - confidence score (if available)

---

### 3.4 OCR Output Formats

- OCR results must be available in:
  - Plain text
  - Markdown
  - JSON
- All formats must be derived from the same OCR result.

---

### 3.5 Schema-Based Structured Extraction

#### 3.5.1 Schema Definition

- Users must be able to define reusable schemas.
- Each schema consists of multiple fields.
- Each field must have:
  - name
  - type (string, number, boolean, date, enum)
  - required flag
  - description
- Field names must be unique within a schema.
- Schemas must be owned by users.

---

#### 3.5.2 Schema Management

- The system must support creating, updating, deleting, and listing schemas.
- Schema validation must ensure:
  - valid field types
  - unique field names
  - field count limits
- Schema definitions must be stored persistently.

---

#### 3.5.3 Structured Extraction Execution

- Users must be able to execute structured extraction on a document using a selected schema.
- Structured extraction must use OCR text as input.
- Extracted values must be normalized to their schema-defined types.
- Required fields must be validated.
- Each extracted field must include a confidence score.
- Structured extraction results must be stored persistently.

---

### 3.6 Structured Extraction Output

- Structured extraction results must be returned as JSON.
- Output must include:
  - schema identifier
  - extracted field values
  - confidence scores
  - validation status

Example:
```json
{
  "schema": "Invoice Schema",
  "fields": {
    "invoice_number": {
      "value": "INV-1001",
      "confidence": 0.92
    },
    "total_amount": {
      "value": 12500,
      "confidence": 0.89
    }
  },
  "validation": {
    "is_valid": true,
    "missing_fields": []
  }
}
```

---

### 3.7 API Access

- All functionality must be exposed via REST APIs.
- APIs must support retrieving:
  - document metadata
  - OCR results
  - structured extraction results
- APIs must enforce authentication and authorization.

---

## 4. Non-Functional Requirements

### 4.1 Security

- JWT authentication must be enforced.
- User data must be isolated.
- Files must not be publicly accessible.
- Input validation must be applied to all endpoints.
- Rate limiting must be applied to uploads and OCR requests.

---

### 4.2 Performance

- OCR and structured extraction must be asynchronous.
- API must remain responsive under load.
- Large documents must be handled safely.

---

### 4.3 Scalability

- Backend must be stateless.
- OCR workers must be horizontally scalable.
- Database queries must be optimized using indexes.

---

### 4.4 Reliability

- OCR job failures must be handled gracefully.
- Retry mechanisms must be implemented with limits.
- Failed or partial jobs must be observable.

---

### 4.5 Observability

- Structured logging must be implemented.
- Errors must be traceable.
- Job status must be visible.

---

## 5. Data Entities

- User
- Document
- OCRResult
- SchemaTemplate
- SchemaField
- StructuredExtractionResult

All entities must include:
- created_at
- updated_at

---

## 6. Constraints & Limits

- Maximum file size per upload
- Maximum documents per user
- Maximum schemas per user
- Maximum fields per schema
- Maximum OCR jobs per user

---

## 7. Out of Scope (Initial Version)

- Handwriting-specific OCR optimization
- Nested or conditional schemas
- Automatic schema generation
- Cross-document search
- Frontend implementation

---

## 8. Success Criteria

The backend is considered complete when:
- Users can upload documents and extract OCR text
- OCR processing is asynchronous and scalable
- Schema-based extraction produces validated structured output
- User data is fully isolated and secure
- The service can be deployed to production
