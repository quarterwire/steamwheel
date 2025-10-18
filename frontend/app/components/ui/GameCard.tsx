import { Badge } from './badge'
import { Play, Star } from 'lucide-react'
import { BsPlaystation, BsSteam } from 'react-icons/bs'
import { FaRegCirclePlay } from 'react-icons/fa6'
import { FaXbox } from 'react-icons/fa'
import { FaStar } from 'react-icons/fa6'
import { Button } from './button'

const GameCard = ({
  title,
  publisher,
  year,
  ratings,
  stores,
  genres,
  description,
  video,
  cover,
}: {
  title: string
  publisher: string
  year: number
  ratings: number
  stores: string[]
  genres: string[]
  description: string
  video: string
  cover: string
}) => {
  return (
    <>
      <div className="flex bg-card rounded-md w-fit">
        <div className="flex flex-col gap-5 bg-background p-7 py-5">
          <img src={cover} className="rounded-md" />
          <div className="border rounded-md border-zinc-500 bg-card/50 ">
            <div className="flex justify-between bg-card items-center  rounded-t-md p-3">
              <span className="text-sm">Where to play</span>
              <span className="flex items-center gap-2 text-primary">
                <FaRegCirclePlay />
                Trailer
              </span>
            </div>
            <div>
              <ul className="flex flex-col p-3 gap-3">
                {stores.map((store, i) => (
                  <li className="flex items-center gap-2">
                    <BsSteam />
                    <span className="text-sm">{store}</span>
                    <Button size={'icon-sm'}>
                      <Play size={8} />
                    </Button>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
        <div className="p-4 flex flex-col gap-10">
          <div className="space-y-2">
            <div>
              <div className="flex gap-4 items-end font-serif">
                <h1>{title}</h1>
                <h2 className="underline text-muted">{year}</h2>
              </div>
              <p>
                <span className="text-muted">Published by</span>{' '}
                <span className="underline">{publisher}</span>
              </p>
            </div>

            <div className="flex flex-col gap-2">
              <div className="flex gap-2">
                <p>Ratings:</p>
                <ul className="flex gap-1 items-center">
                  {[...Array(ratings)].map((x, i) => (
                    <FaStar key={i} />
                  ))}
                </ul>
              </div>
              <div className="flex gap-2">
                <p>Genres:</p>
                <ul className="flex gap-1 t">
                  {genres.map((genre, i) => (
                    <Badge variant="default" key={i} className="text-[9px] bg-zinc-600">
                      {genre}
                    </Badge>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          <p className="w-[75ch] object-cover">{description}</p>
          <div>
            <iframe
              width="566"
              height="300"
              src={`https://www.youtube.com/embed/${video}`}
            ></iframe>
          </div>
        </div>
      </div>
    </>
  )
}

export default GameCard
