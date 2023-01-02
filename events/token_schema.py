from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class User(BaseModel):
    _ref: str = Field(..., alias='$ref')


class ProviderId(BaseModel):
    type: str


class _TokenResponse(BaseModel):
    _ref: str = Field(..., alias='$ref')


class OperationType(BaseModel):
    type: str


class Properties(BaseModel):
    user: User
    providerId: ProviderId
    _tokenResponse: _TokenResponse
    operationType: OperationType


class Welcome4(BaseModel):
    type: str
    additionalProperties: bool
    properties: Properties
    required: List[str]
    title: str


class FederatedId(BaseModel):
    type: str
    format: str
    qt_uri_protocols: List[str] = Field(..., alias='qt-uri-protocols')


class ProviderId1(BaseModel):
    type: str


class Email(BaseModel):
    type: str


class EmailVerified(BaseModel):
    type: str


class FirstName(BaseModel):
    type: str


class FullName(BaseModel):
    type: str


class LastName(BaseModel):
    type: str


class PhotoUrl(BaseModel):
    type: str
    format: str
    qt_uri_protocols: List[str] = Field(..., alias='qt-uri-protocols')


class LocalId(BaseModel):
    type: str


class DisplayName(BaseModel):
    type: str


class IdToken(BaseModel):
    type: str


class Context(BaseModel):
    type: str


class OauthAccessToken(BaseModel):
    type: str


class OauthExpireIn(BaseModel):
    type: str


class RefreshToken(BaseModel):
    type: str


class ExpiresIn(BaseModel):
    type: str
    format: str


class OauthIdToken(BaseModel):
    type: str


class RawUserInfo(BaseModel):
    type: str


class Kind(BaseModel):
    type: str


class Properties1(BaseModel):
    federatedId: FederatedId
    providerId: ProviderId1
    email: Email
    emailVerified: EmailVerified
    firstName: FirstName
    fullName: FullName
    lastName: LastName
    photoUrl: PhotoUrl
    localId: LocalId
    displayName: DisplayName
    idToken: IdToken
    context: Context
    oauthAccessToken: OauthAccessToken
    oauthExpireIn: OauthExpireIn
    refreshToken: RefreshToken
    expiresIn: ExpiresIn
    oauthIdToken: OauthIdToken
    rawUserInfo: RawUserInfo
    kind: Kind


class TokenResponse(BaseModel):
    type: str
    additionalProperties: bool
    properties: Properties1
    required: List[str]
    title: str


class Uid(BaseModel):
    type: str


class Email1(BaseModel):
    type: str


class EmailVerified1(BaseModel):
    type: str


class DisplayName1(BaseModel):
    type: str


class IsAnonymous(BaseModel):
    type: str


class PhotoURL(BaseModel):
    type: str
    format: str
    qt_uri_protocols: List[str] = Field(..., alias='qt-uri-protocols')


class Items(BaseModel):
    _ref: str = Field(..., alias='$ref')


class ProviderData(BaseModel):
    type: str
    items: Items


class StsTokenManager(BaseModel):
    _ref: str = Field(..., alias='$ref')


class CreatedAt(BaseModel):
    type: str


class LastLoginAt(BaseModel):
    type: str


class ApiKey(BaseModel):
    type: str


class AppName(BaseModel):
    type: str


class Properties2(BaseModel):
    uid: Uid
    email: Email1
    emailVerified: EmailVerified1
    displayName: DisplayName1
    isAnonymous: IsAnonymous
    photoURL: PhotoURL
    providerData: ProviderData
    stsTokenManager: StsTokenManager
    createdAt: CreatedAt
    lastLoginAt: LastLoginAt
    apiKey: ApiKey
    appName: AppName


class User1(BaseModel):
    type: str
    additionalProperties: bool
    properties: Properties2
    required: List[str]
    title: str


class ProviderId2(BaseModel):
    type: str


class Uid1(BaseModel):
    type: str


class DisplayName2(BaseModel):
    type: str


class Email2(BaseModel):
    type: str


class PhoneNumber(BaseModel):
    type: str


class PhotoURL1(BaseModel):
    type: str
    format: str
    qt_uri_protocols: List[str] = Field(..., alias='qt-uri-protocols')


class Properties3(BaseModel):
    providerId: ProviderId2
    uid: Uid1
    displayName: DisplayName2
    email: Email2
    phoneNumber: PhoneNumber
    photoURL: PhotoURL1


class ProviderDatum(BaseModel):
    type: str
    additionalProperties: bool
    properties: Properties3
    required: List[str]
    title: str


class RefreshToken1(BaseModel):
    type: str


class AccessToken(BaseModel):
    type: str


class ExpirationTime(BaseModel):
    type: str


class Properties4(BaseModel):
    refreshToken: RefreshToken1
    accessToken: AccessToken
    expirationTime: ExpirationTime


class StsTokenManager1(BaseModel):
    type: str
    additionalProperties: bool
    properties: Properties4
    required: List[str]
    title: str


class Definitions(BaseModel):
    Welcome4: Welcome4
    TokenResponse: TokenResponse
    User: User1
    ProviderDatum: ProviderDatum
    StsTokenManager: StsTokenManager1


class TokenSchema(BaseModel):
    _schema: str = Field(..., alias='$schema')
    _ref: str = Field(..., alias='$ref')
    definitions: Definitions
