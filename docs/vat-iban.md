# VAT and IBAN Validation API

Two financial validations in one API. **EU VAT numbers** are checked against the **official VIES service** of the European Commission — a real, live validation, not a format guess — alongside current **VAT rates for every EU country**. **IBANs** are validated (structure, checksum, national check digits) and enriched with **bank name and BIC/SWIFT** lookup.

**Live on RapidAPI → [VAT and IBAN Validation API](https://rapidapi.com/Hitler-HlDevZDwP/api/vat-and-iban-validation-api1)**

**Gateway host:** `vat-and-iban-validation-api1.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/vat`

Every call goes to `https://vat-and-iban-validation-api1.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `vat-and-iban-validation-api1.p.rapidapi.com` |

## Endpoints

### `GET /vat/validate?country=DE&number=811569869`

Validate an EU VAT number against **VIES**, the official EU database. Pass the country code and the number without the country prefix (or pass the full number as `vat=DE811569869`). The response reports `valid: true/false` plus the registered name and address when the member state publishes them — e.g. SAP's real German VAT number DE811569869 validates as `valid: true`.

> **Note:** UK (GB) VAT numbers are **not** part of VIES since Brexit. For GB numbers the API answers honestly that the check is outside VIES coverage instead of guessing.

### `GET /vat/rates?country=DE`

Current standard and reduced **VAT rates** for EU countries (reference data, January 2026). Omit `country` for the full EU list.

### `GET /iban/validate?iban=DE89370400440532013000`

Validate an IBAN and look up its bank.

**Response:** JSON like:

```json
{
  "iban": "DE89370400440532013000",
  "formatted": "DE89 3704 0044 0532 0130 00",
  "valid": true,
  "country_code": "DE",
  "bank_code": "37040044",
  "account_number": "0532013000",
  "bic": "COBADEFFXXX",
  "bank_name": "Commerzbank",
  "in_sepa_zone": true
}
```

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl "https://vat-and-iban-validation-api1.p.rapidapi.com/iban/validate?iban=DE89370400440532013000" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: vat-and-iban-validation-api1.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $5 / month | 3,000 / month |
| ULTRA | $15 / month | 10,000 / month |
| MEGA | $29 / month | 40,000 / month |

Paid plans are soft limits with per-request overage ($0.003 PRO / $0.002 ULTRA / $0.001 MEGA).

Subscribe and manage your plan here: **[VAT and IBAN Validation API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/vat-and-iban-validation-api1)**

Part of the [hhelll API family](../README.md#the-api-catalog).
