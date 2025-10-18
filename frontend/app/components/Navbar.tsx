import { FerrisWheelIcon, Search } from 'lucide-react'
import { Link } from 'react-router'
import { Button } from './ui/button'
import { Input } from './ui/input'
import { InputGroup, InputGroupAddon, InputGroupInput } from './ui/input-group'

const Navbar = () => {
  return (
    <header className="fixed top-0 z-50 w-full bg-white/80 backdrop-blur-sm shadow-sm dark:bg-gray-950/80">
      <div className="container mx-auto flex h-16 max-w-7xl items-center justify-between px-4 md:px-6 ">
        <Link href="#" className="flex items-center gap-2" prefetch={false}>
          <FerrisWheelIcon className="h-6 w-6" />
          <span className="text-lg font-bold">SteamWheel</span>
        </Link>
        <nav className="hidden space-x-6 md:flex md:items-center">
          <Link
            href="#"
            className="text-sm font-medium hover:text-gray-900 dark:hover:text-gray-50"
            prefetch={false}
          >
            <InputGroup>
              <InputGroupInput placeholder="Search..." />
              <InputGroupAddon>
                <Search />
              </InputGroupAddon>
            </InputGroup>{' '}
          </Link>
          <Button>Get a random game</Button>
        </nav>
      </div>
    </header>
  )
}

export default Navbar
