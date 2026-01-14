import React from 'react';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';
import type { Area } from 'volto-lactec-intranet/types/content';

interface AreaInfoProps {
  content: Area;
}

const AreaInfo: React.FC<AreaInfoProps> = ({ content }) => {
  const { area } = content;

  return (
    <UniversalLink className={'area'} item={area}>
      {area.title} - {area.description}
    </UniversalLink>
  );
};

export default AreaInfo;
