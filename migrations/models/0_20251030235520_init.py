from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "customer" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "order" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(9) NOT NULL DEFAULT 'Draft' /* DRAFT: Draft\nCONFIRMED: Confirmed\nSHIPPED: Shipped */,
    "customer_id" CHAR(36) NOT NULL REFERENCES "customer" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "orderitem" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "product_name" VARCHAR(255) NOT NULL,
    "quantity" SMALLINT NOT NULL,
    "price" REAL NOT NULL,
    "order_id" CHAR(36) NOT NULL REFERENCES "order" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmW1vozgQx78K4lVP2qt20267rU4n0YSo3OahStK70z4IueAkVsGmxlw3qvLdzzYYiI"
    "Fs6XX3Eilv2vCfGWz/GHsm5MkMiQ+D+LibxIyEkJqXxpOJQQj5h4rtjWGCKCosQmDgLpDO"
    "XtnrLmYUeIzrcxDEkEs+jD2KIoYI5ipOgkCIxOOOCC8KKcHoIYEuIwvIlnI+n79yGWEffo"
    "Oxuozu3TmCgb8xXeSLsaXuslUktdtbp9eXnmK4O9cjQRLiwjtasSXBuXuSIP9YxAjbAmJI"
    "AYN+aRliltmKlZTOmAuMJjCfql8IPpyDJBAwzN/mCfYEA0OOJP6c/m62wOMRLNAizASLp3"
    "W6qmLNUjXFUN1ra3J0cvaLXCWJ2YJKoyRirmUgYCANlVwLkPJ/BWV3CWg9SuWvweQTfQlG"
    "JRQcixxSIBWgl1EzQ/DNDSBesCW/7Lx/vwXjn9ZEkuReEiXheZ0m/CgzdVKbQFoghCFAQR"
    "uGecDrQPx+Lu4kQrG35/elpBTCHfDuHwH13Q1LwZpQH9K4Cvsqi+t/nMAAyBVW+WZn3Fjc"
    "Yzezda1SRanZ05SwSIc00aqawk6oKwCDhZy1GFuMtMGjphjkoJorAcldDmVgn8sAN9SUgR"
    "5XGQphPU4VowH1s6Bj9WE3t5pJIfDHOFipLdbMdeYM7enMGt6IlYRx/BBIONbMFpaOVFea"
    "enSmnX/5TYy/nNm1IS6NT+ORrT+s3G/2yRRzAgkjLiaPLvBLCaZUBWajIMUMsKTmkBQVyc"
    "ZJKB+nw2kA7MHKYy2if16NN3sUzFl1V5i9idWfXRrS/AV3x6O+MxnavUujS/Ac0RD6X/D0"
    "2rm5Edp0iaIIponasqpdPKOmXTRWtAu9JVANstvugNLCXvOk+mm16wUHU6UTqIKsUuwTCt"
    "ECf4SrSjrXl/3yV5udpVep/Fym4DEvfXqK8GXyxUGW7m9r2rV6trl+diflIgbD12inHH6f"
    "/QL741sqyaSprVLAvtNaIeV2aK/2ub2KKPETj7ltv23rcYdv3TnShwRghtiqinMagiBwMK"
    "tHWo7TcIrDYTdxLsQ4v550zs8+cKuchrg434J1OrQGA2c007BFFHk1KdgPCGgAlkdotOYi"
    "ZDd5bcHSG99eDWzjZmJ3nakzHm0279IoJC6gtKhObGugMcxKZ6vDsRxz6OuK9wb/sanbw3"
    "c5ekdXzoy27dyP7GEs3n14y7oGJrNs7V5A4bMzrUtjTajdljXVIHt8/+vL2LQUdN6dnp9+"
    "ODk7zetBrmwrCqoeNHcq/0AaZ+3+c5uUUsihP8lBiq3RAmLmvp8A3719+wyA3KsRoLRp71"
    "AIZjDdg5sQ/5iORw3vT4oQDeQt5gv87COPvTECFLOvu4l1C0Wx6o33jwre0dD6W+faHYyv"
    "9KIsbnDV7neX1y8v638BZk3aRw=="
)
