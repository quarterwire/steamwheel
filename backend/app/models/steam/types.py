from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Union


# ----- Requirements -----
class Requirements(BaseModel):
    minimum: Optional[str] = None
    recommended: Optional[str] = None


# ----- Pricing -----
class PriceOverview(BaseModel):
    currency: str
    initial: int
    final: int
    discount_percent: int
    initial_formatted: str
    final_formatted: str


# ----- Platforms -----
class Platforms(BaseModel):
    windows: bool
    mac: bool
    linux: bool


# ----- Metacritic -----
class Metacritic(BaseModel):
    score: int | None
    url: str | None


# ----- Categories / Genres -----
class Category(BaseModel):
    id: int
    description: str


class Genre(BaseModel):
    id: Union[str, int]  # sometimes numeric, sometimes string
    description: str


# ----- Screenshots -----
class Screenshot(BaseModel):
    id: int
    path_thumbnail: str
    path_full: str


# ----- Videos -----
class Webm(BaseModel):
    f480: str = Field(..., alias="480")
    max: str


class Mp4(BaseModel):
    f480: str = Field(..., alias="480")
    max: str


class Movie(BaseModel):
    id: int
    name: str
    thumbnail: str
    webm: Optional[Webm] = None
    mp4: Optional[Mp4] = None
    dash_av1: Optional[str] = None
    dash_h264: Optional[str] = None
    hls_h264: Optional[str] = None
    highlight: Optional[bool] = None


# ----- Miscellaneous -----
class Recommendations(BaseModel):
    total: Optional[int] = 0


class ReleaseDate(BaseModel):
    coming_soon: bool
    date: str


# ----- Ratings -----
class Esrb(BaseModel):
    rating: Optional[str] = None
    descriptors: Optional[str] = None


class Kgrb(BaseModel):
    rating: Optional[str] = None
    descriptors: Optional[str] = None


class Pegi(BaseModel):
    rating: Optional[str] = None


class Bbfc(BaseModel):
    rating: Optional[str] = None


class Usk(BaseModel):
    rating: Optional[str] = None


class Oflc(BaseModel):
    rating: Optional[str] = None


class Nzoflc(BaseModel):
    rating: Optional[str] = None


class Crl(BaseModel):
    rating: Optional[str] = None


class Ratings(BaseModel):
    esrb: Optional[Esrb] = None
    kgrb: Optional[Kgrb] = None
    pegi: Optional[Pegi] = None
    bbfc: Optional[Bbfc] = None
    usk: Optional[Usk] = None
    oflc: Optional[Oflc] = None
    nzoflc: Optional[Nzoflc] = None
    crl: Optional[Crl] = None


# ----- Main App Data -----
class Data(BaseModel):
    type: str
    name: str
    steam_appid: int
    required_age: Optional[int] = None
    is_free: bool
    dlc: Optional[List[int]] = None
    detailed_description: Optional[str] = None
    about_the_game: Optional[str] = None
    short_description: Optional[str] = None
    supported_languages: Optional[str] = None
    header_image: Optional[str] = None
    capsule_image: Optional[str] = None
    capsule_imagev5: Optional[str] = None
    website: Optional[str] = None

    pc_requirements: Optional[Union[Requirements, list]] = None
    mac_requirements: Optional[Union[Requirements, list]] = None
    linux_requirements: Optional[Union[Requirements, list]] = None

    legal_notice: Optional[str] = None
    developers: Optional[List[str]] = []
    publishers: Optional[List[str]] = []

    price_overview: Optional[PriceOverview] = None
    packages: Optional[List[int]] = []
    platforms: Optional[Platforms] = None
    metacritic: Optional[Metacritic] = None
    categories: Optional[List[Category]] = []
    genres: Optional[List[Genre]] = []
    screenshots: Optional[List[Screenshot]] = []
    movies: Optional[List[Movie]] = []
    recommendations: Optional[Recommendations] = None
    release_date: Optional[ReleaseDate] = None
    background: Optional[str] = None
    background_raw: Optional[str] = None
    ratings: Optional[Ratings] = None | str

    # --- Validators to normalize inconsistent data ---
    @field_validator(
        "pc_requirements", "mac_requirements", "linux_requirements", mode="before"
    )
    def empty_list_to_none(cls, v):
        if v == []:
            return None
        return v
