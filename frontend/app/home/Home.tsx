import { DicesIcon, Dice6Icon } from 'lucide-react'
import { Button } from '~/components/ui/button'
import GameCard from '~/components/ui/GameCard'

const LandingHeader = () => {
  return (
    <div className="flex flex-col gap-4 items-center">
      <h1 className="!text-6xl font-serif text-center">Get a random game to enjoy</h1>
      <p className="text-center text-muted w-[80ch] mx-auto leading-loose mb-6">
        Can’t decide what to play? SteamWheel randomly selects hidden gems from IGDB for you to
        explore.
      </p>
      <Button size={'lg'} className="w-fit !px-8 text-lg mb-6">
        <DicesIcon size={24} /> Surprise Me
      </Button>
      <GameCard
        title="Helldivers 2"
        publisher="Arrowhead Game Studios"
        year={2024}
        stores={['Playstation', 'Xbox', 'Steam']}
        cover="https://images.igdb.com/igdb/image/upload/t_cover_big/coabbf.webp"
        ratings={4}
        genres={['Tactical', 'Shooter']}
        video="WsYK0Y6mjFE"
        description="The Galaxy’s Last Line of Offence. Enlist in the Helldivers and join the fight for freedom across a hostile galaxy in a fast, frantic, and ferocious third-person shooter."
      />
    </div>
  )
}

export default LandingHeader
